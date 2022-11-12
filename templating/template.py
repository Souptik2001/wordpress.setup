import argparse

from jinja2 import Environment, FileSystemLoader

parser=argparse.ArgumentParser()

defaultPHP = "8.0"
# If this is changed then the default WP version of the setup.sh is also to be changed.
defaultWP = "6.1"
defaultNode = "16.x"
defaultMultisite = "no"
defaultMultisiteType = "subdomain"
defaultVIP = "no"

parser.add_argument("--appName", help="Website/application name",required=True)
parser.add_argument("--php", help="PHP version", default=defaultPHP)
parser.add_argument("--wp", help="WordPress version", default=defaultWP)
parser.add_argument("--node", help="Node version", default=defaultNode)
parser.add_argument("--multisite", help="Multisite or not", default=defaultMultisite, required=True, choices=['yes', 'no'])
parser.add_argument("--vip", help="VIP template or not", default=defaultVIP, required=True, choices=['yes', 'no'])
parser.add_argument("--multisiteType", help="Multisite type", default=defaultMultisiteType, choices=['subdomain', 'subdirectory'])

args=parser.parse_args()

phpVer = defaultPHP if (not (args.php and args.php.strip())) else args.php
wpVer = defaultWP if (not (args.wp and args.wp.strip())) else args.wp
nodeVer = defaultNode if (not (args.node and args.node.strip())) else args.node


environment = Environment(loader=FileSystemLoader("templates/"))

# Lando config file
landoConfigTemplate = environment.get_template(".lando.yml.j2")

coreInstallCommand = "wp core install --url=https://$LANDO_APP_NAME.$LANDO_DOMAIN --title=$LANDO_APP_NAME --admin_user=admin --admin_password=admin --admin_email=admin@souptik.dev --skip-email"
queryMonitorInstallCommand = "wp plugin install query-monitor --activate"

if args.multisite and args.multisite == "yes":
	coreInstallCommand = "wp core multisite-install --url=https://$LANDO_APP_NAME.$LANDO_DOMAIN --title=$LANDO_APP_NAME --admin_user=admin --admin_password=admin --admin_email=admin@souptik.dev --skip-email --skip-config"
	queryMonitorInstallCommand = "wp plugin install query-monitor --activate-network"

userCreateCommand = ""
userSuperAdminCommand = ""
vip_mu_plugins_link = ""

if args.vip and args.vip == "yes":
	queryMonitorInstallCommand = ""
	userCreateCommand = "wp user create sadmin sadmin@souptik.dev --role=administrator --user_pass=\"sadmin\""
	userSuperAdminCommand = "wp super-admin add sadmin"

themeInstallCommand = "wp theme install twentytwentytwo --activate"

filename = f"./tmp/.lando.yml"
landoConfigContent = landoConfigTemplate.render(
	app=f"{args.appName}",
	php=f"{phpVer}",
	wp=f"{wpVer}",
	node=f"{nodeVer}",
	core_install_command=coreInstallCommand,
	query_monitor_install_command=queryMonitorInstallCommand,
	user_create_command=userCreateCommand,
	user_super_admin_command=userSuperAdminCommand,
	theme_install_command=themeInstallCommand,
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

vipConf = ""

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

if args.vip and args.vip == "yes":
	vipConf = """
// Load early dependencies
if ( file_exists( __DIR__ . '/wp-content/mu-plugins/000-pre-vip-config/requires.php' ) ) {
	require_once __DIR__ . '/wp-content/mu-plugins/000-pre-vip-config/requires.php';
}
// // Loading the VIP config file
if ( file_exists( __DIR__ . '/wp-content/vip-config/vip-config.php' ) ) {
	require_once __DIR__ . '/wp-content/vip-config/vip-config.php';
}

// Defining constant settings for file permissions and auto-updates
define( 'DISALLOW_FILE_MODS', true );
define( 'VIP_GO_APP_ENVIRONMENT', true );
"""

filename = f"./tmp/wp-config.php"
wpConfigContent = wpConfigTemplate.render(
	app=f"{args.appName}",
	multisite_conf=multiSiteConf,
	vip_template=vipConf
)
with open(filename, mode="w", encoding="utf-8") as message:
	message.write(wpConfigContent)
	print(f"Created: {filename}")
