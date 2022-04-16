#! /bin/bash

###############################################
## Usage check

if (( $# < 2 )); then
	echo "Inappropriate arguments."
	echo "Usage : setup.sh [name_of_the_project] [path/to/the/folder/to/setup/project] [(optional)ssh_or_https_link_to_clone_wp_content_repo]"
	exit 128
fi

# Check if the supplied path exixts - if not exit.

###############################################

echo 'Just 2 mins please!!'
start=`date +%s`


###############################################
## Main Process

# Move to the home directory

cd ~

# Create a new folder in the supplied path named `name_of_the_project`

# HELP: This expression is used to remove trailing slash from a string - `${var_name%/}`

project_folder="$2/$1"

echo " Project folder is being created at location - $project_folder"
mkdir "$project_folder"

# Create copy the `.lando.yml`, `wp-config.php`, `.lando` to that folder.

cp ~/wordpress/wordpress.setup-DO-NOT-DELETE/.lando.yml "$project_folder/.lando.yml"
cp -r ~/wordpress/wordpress.setup-DO-NOT-DELETE/.lando "$project_folder/.lando"
cp ~/wordpress/wordpress.setup-DO-NOT-DELETE/wp-config.php "$project_folder/wp-config.php"


# Clone the repo with the name `wp-content`.

cd $project_folder

git clone $3 wp-content

# If clone fails and `wp-content` is not present then copy this `wp-content` there.

# Set envionment variables # This needs to be exported which this needs to be unique.

export SD_WP_LANDO_APP_NAME=$1

# Run `lando start`

lando start

###############################################

end=`date +%s`

runtime=$((end-start))

echo "You see it's done and it took only $runtime seconds! Enjoy! ~ Souptik Datta"