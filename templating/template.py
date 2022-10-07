import argparse

from jinja2 import Environment, FileSystemLoader

parser=argparse.ArgumentParser()

defaultPHP = "8.0"
defaultWP = "6.0.2"
defaultNode = "16.x"

parser.add_argument("--appName", help="Website/application name",required=True)
parser.add_argument("--php", help="PHP version", default=defaultPHP)
parser.add_argument("--wp", help="WordPress version", default=defaultWP)
parser.add_argument("--node", help="Node version", default=defaultNode)

args=parser.parse_args()

phpVer = "8.0" if (not (args.php and args.php.strip())) else args.php
wpVer = "6.0.2" if (not (args.wp and args.wp.strip())) else args.wp
nodeVer = "16.x" if (not (args.node and args.node.strip())) else args.node


environment = Environment(loader=FileSystemLoader("templates/"))

# Lando config file
landoConfigTemplate = environment.get_template(".lando.yml.j2")

filename = f"./tmp/.lando.yml"
landoConfigContent = landoConfigTemplate.render(
	app=f"{args.appName}",
	php=f"{phpVer}",
	wp=f"{wpVer}",
	node=f"{nodeVer}"
)
with open(filename, mode="w", encoding="utf-8") as message:
	message.write(landoConfigContent)
	print(f"Created: {filename}")

# WordPress config file
wpConfigTemplate = environment.get_template("wp-config.php.j2")

filename = f"./tmp/wp-config.php"
wpConfigContent = wpConfigTemplate.render()
with open(filename, mode="w", encoding="utf-8") as message:
	message.write(wpConfigContent)
	print(f"Created: {filename}")
