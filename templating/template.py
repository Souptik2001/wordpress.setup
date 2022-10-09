import argparse

from jinja2 import Environment, FileSystemLoader

parser=argparse.ArgumentParser()

defaultPHP = "8.0"
defaultWP = "5.9"
defaultNode = "16.x"

parser.add_argument("--appName", help="Website/application name",required=True)
parser.add_argument("--php", help="PHP version", default=defaultPHP)
parser.add_argument("--wp", help="WordPress version", default=defaultWP)
parser.add_argument("--node", help="Node version", default=defaultNode)
parser.add_argument("--multisite", help="Multisite or not", default=defaultNode, required=True, choices=['yes', 'no'])
parser.add_argument("--multisiteType", help="Multisite type", default=defaultNode, choices=['subdomain', 'subdirectory'])

args=parser.parse_args()

phpVer = defaultPHP if (not (args.php and args.php.strip())) else args.php
wpVer = defaultWP if (not (args.wp and args.wp.strip())) else args.wp
nodeVer = defaultNode if (not (args.node and args.node.strip())) else args.node


environment = Environment(loader=FileSystemLoader("templates/"))

# Lando config file
landoConfigTemplate = environment.get_template(".lando.yml.j2")

coreInstallCommand = "wp core install --url=https://$LANDO_APP_NAME.$LANDO_DOMAIN --title=$LANDO_APP_NAME --admin_user=admin --admin_password=admin --admin_email=admin@souptik.dev --skip-email"

if args.multisite and args.multisite == "yes":
	coreInstallCommand = "wp core multisite-install --url=https://$LANDO_APP_NAME.$LANDO_DOMAIN --title=$LANDO_APP_NAME --admin_user=admin --admin_password=admin --admin_email=admin@souptik.dev --skip-email --skip-config"

filename = f"./tmp/.lando.yml"
landoConfigContent = landoConfigTemplate.render(
	app=f"{args.appName}",
	php=f"{phpVer}",
	wp=f"{wpVer}",
	node=f"{nodeVer}",
	core_install_command=coreInstallCommand
)
with open(filename, mode="w", encoding="utf-8") as message:
	message.write(landoConfigContent)
	print(f"Created: {filename}")

# WordPress config file
wpConfigTemplate = environment.get_template("wp-config.php.j2")


multiSiteConf = f"""
define('WP_ALLOW_MULTISITE', true);
define( 'MULTISITE', true );
define( 'DOMAIN_CURRENT_SITE', '{args.appName}.lndo.site' );
define( 'PATH_CURRENT_SITE', '/' );
define( 'SITE_ID_CURRENT_SITE', 1 );
define( 'BLOG_ID_CURRENT_SITE', 1 );
"""

if args.multisiteType and args.multisiteType == "subdirectory":
	multiSiteConf += "define( 'SUBDOMAIN_INSTALL', false );"
else:
	multiSiteConf += "define( 'SUBDOMAIN_INSTALL', true );"

if args.multisite and args.multisite == "no":
	multiSiteConf = ""
	coreInstallCommand = """
	wp core install --url=https://$LANDO_APP_NAME.$LANDO_DOMAIN \
	--title=$LANDO_APP_NAME \
	--admin_user=admin \
	--admin_password=admin \
	--admin_email=admin@souptik.dev \
	--skip-email
	"""

filename = f"./tmp/wp-config.php"
wpConfigContent = wpConfigTemplate.render(
	multisite_conf=multiSiteConf
)
with open(filename, mode="w", encoding="utf-8") as message:
	message.write(wpConfigContent)
	print(f"Created: {filename}")
