#! /bin/bash

###############################################
## Usage check

usage() {
	echo -e '
========== HELP MENU ==========

Usage: \033[1msetup.sh [name_of_the_project] [path/to/the/folder/to/setup/project] [(optional)ssh_or_https_link_to_clone_wp_content_repo]\033[0m

Arguments:
--wp : WordPress version.
--php: PHP version.
--node: Node version.
--multisite: Whether to create multisite or single site. yes OR no.
--multisitetype: Type of multisite. subdomain OR subdirectory.
--vip: Whether to create VIP template site or not. yes OR no.
--help: Display this help menu.

Example: \033[1msetup.sh [project_name] ~/wordpress --multisite=yes --vip=yes git@github.com:[repo]\033[0m

===============================
'
}

# \033[1m\033[0m

# Read command line options
ARGUMENT_LIST=(
    "wp:"
    "php:"
    "node:"
	"multisite:"
	"multisitetype:"
	"vip:"
	"help"
)

# read arguments
opts=$(getopt \
    --longoptions "$(printf "%s," "${ARGUMENT_LIST[@]}")" \
    --name "$(basename "$0")" \
    --options "" \
    -- "$@"
)

eval set --$opts

while true; do
    case "$1" in
    --wp)
        shift
        wp=$1
        ;;
    --php)
        shift
        php=$1
        ;;
    --node)
        shift
        node=$1
        ;;
	--multisite)
		shift
		multisite=$1
		;;
	--multisitetype)
		shift
		multisitetype=$1
		;;
	--vip)
		shift
		vip=$1
		;;
	--help)
		shift
		usage
		exit 128
		;;
      --)
        shift
        break
        ;;
    esac
    shift
done

if (( $# < 2 )); then
	echo "ERROR : Inappropriate arguments."
	echo "Use setup.sh --help for help."
	echo "Usage : setup.sh [name_of_the_project] [path/to/the/folder/to/setup/project] [(optional)ssh_or_https_link_to_clone_wp_content_repo]"
	exit 128
fi

# Check if the supplied path exixts - if not exit.

if [[ ! -d "$2/" ]]
then
    echo "ERROR : $2 does not exists on your filesystem."
	echo "Use setup.sh --help for help."
	echo "Usage : setup.sh [name_of_the_project] [path/to/the/folder/to/setup/project] [(optional)ssh_or_https_link_to_clone_wp_content_repo]"
	exit 128
fi

if [[ ! -d ~/wordpress/wordpress.setup-DO-NOT-DELETE/ ]]
then
	echo "ERROR : The folder ~/wordpress/wordpress.setup-DO-NOT-DELETE/ doesn't exists."
	echo "Make sure that folder is present and all the nessesary components are present inside that as it will be used."
	exit 128
fi

project_folder="$2/$1"

if [[ -d $project_folder ]]
then
	echo "ERROR : The project already exists at ( $project_folder )."
	echo "Please remove the already existing project and try again."
	exit 128
fi


###############################################

echo 'Just 2 mins please!!'
start=`date +%s`


###############################################
## Main Process

if [ -z "$multisite" ]
then
    multisite="no"
fi

if [ -z "$multisitetype" ]
then
    multisitetype="subdomain"
fi

if [ -z "$vip" ]
then
	vip="no"
fi

## Had to define default WP version here because this is required in other parts of this script also other than just the python line.
## If this is changed then the value of defaultWP in the `template.py` script also needs to be changed.
if [ -z "$wp" ]
then
    wp="6.2.2"
fi

# Download WordPress core

cd ~/wordpress/wordpress.setup-DO-NOT-DELETE

if [[ ! -d "wordpress-core-$wp" ]]
then
	wget "https://wordpress.org/wordpress-$wp.tar.gz"
	if [ $? -ne 0 ]; then
		echo "ERROR: WordPress core download error."
		exit 128
	fi
	tar -xf "wordpress-$wp.tar.gz"
	rm "wordpress-$wp.tar.gz"
	mv wordpress "wordpress-core-$wp"
fi

# Cleanup..🧹 - Clean up any existing previous template files

cd ~/wordpress/wordpress.setup-DO-NOT-DELETE/templating

if [[ -d ~/wordpress/wordpress.setup-DO-NOT-DELETE/tmp ]]
then
	rm -r tmp
fi

mkdir tmp

# Run the templating script to generate the files..

python template.py --appName=$1 --php=$php --wp=$wp --node=$node --multisite=$multisite --multisiteType=$multisitetype --vip=$vip

if [ $? -ne 0 ]; then
	echo "ERROR: Templating script error."
	exit 128
fi

# Move to the home directory

cd ~

# Create a new folder in the supplied path named `name_of_the_project`

# HELP: This expression is used to remove trailing slash from a string - `${var_name%/}`

echo " Project folder is being created at location - $project_folder"
mkdir "$project_folder"

if [[ ! -d "$project_folder/" ]]
then
    echo "ERROR : Project folder( $project_folder ) not found."
	echo "Somehow the folder didn't get created. Do you see any other errors above?"
	exit 128
fi

# Create copy the `.lando.yml`, `wp-config.php`, `.lando` to that folder.

cp ~/wordpress/wordpress.setup-DO-NOT-DELETE/templating/tmp/.lando.yml "$project_folder/.lando.yml"
cp -r ~/wordpress/wordpress.setup-DO-NOT-DELETE/.lando "$project_folder/.lando"
cp ~/wordpress/wordpress.setup-DO-NOT-DELETE/templating/tmp/wp-config.php "$project_folder/wp-config.php"

# Clean up..🧹 - Remove the created files
rm -r ~/wordpress/wordpress.setup-DO-NOT-DELETE/templating/tmp

# Clone the repo with the name `wp-content`.

cd $project_folder

if (( $# > 2 )); then
	git clone $3 wp-content
else
	echo "INFO : NO wp-content directory GIT URL provided. Copying the default wp-content directory."
	cp -r ~/wordpress/wordpress.setup-DO-NOT-DELETE/wp-content ./wp-content
fi

# If clone fails and `wp-content` is not present then copy this `wp-content` there.

if [[ -d "wp-content/mu-plugins" ]]
then
	if [[ ! -d "wp-content/client-mu-plugins" ]]
	then
		mv wp-content/mu-plugins wp-content/client-mu-plugins
	else
		rm -r wp-content/mu-plugins
	fi
fi

# Download VIP mu-plugins if VIP and create a sym-link.

cd ~/wordpress/wordpress.setup-DO-NOT-DELETE

if [ "$vip" == "yes" ]; then

	if [[ ! -d "vip-go-mu-plugins" ]]
	then
		git clone git@github.com:Automattic/vip-go-mu-plugins.git --recursive
		if [ $? -ne 0 ]; then
			echo "ERROR: VIP mu-plugins download error."
			exit 128
		fi
	fi

	cp -r ./vip-go-mu-plugins $project_folder/wp-content/mu-plugins

fi

############ Not needed here now, as templating is handled by Jinja.

# Set envionment variables # This needs to be exported which this needs to be unique.

# -i -> Replace the contents in file.
# -n -> Don't print the final output in stdout

# sed '1 s/SD_WP_LANDO_APP_NAME/'$1'/' -i $project_folder'/.lando.yml'

############

# Create the salts.

cd $project_folder

# Run `lando start`

lando start

ln -s ~/wordpress/wordpress.setup-DO-NOT-DELETE/wordpress-core-"$wp" $project_folder'/wordpress'

###############################################

end=`date +%s`

runtime=$((end-start))

echo "Your project is ready at $project_folder."
echo "You see it's done and it took only $runtime seconds! Enjoy!"
echo -e "Visit \033[1mhttps://souptik.dev\033[0m for more projects like this.👋"
