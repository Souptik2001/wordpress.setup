# My WordPress Lando Setup ~ Souptik Datta

**Many folder structure conventions are my personal choice. If you want to edit the folder structure then make sure to change the places where this folder structure is used(mainly in the `.lando.yml` and `setup.sh` files), otherwise the setup will break.**

**Along with the super easy setup one more benefit you will get is that wordpress-core will be present only once, yet providing the flexibility to edit customizable files like `wp-config.php`, `wp-contents` directory, server and php configuration files, etc.**

## Before Using:

- Before using my this setup be sure you have the following things installed (External dependencies):
  - `Docker`.
  - `Lando`.
  - `git`.

## Steps to set-up:

- Clone this repo in folder `~/wordpress/` using the command:
```bash
git clone https://github.com/Souptik2001/wordpress.setup.git ~/wordpress/wordpress.setup-DO-NOT-DELETE
```
OR
```bash
git clone git@github.com:Souptik2001/wordpress.setup.git ~/wordpress/wordpress.setup-DO-NOT-DELETE
```
**( The name used here `wordpress.setup-DO-NOT-DELETE` is important because that name is used in the lando config file ).**
- Now you can just run `lando start` here only and that's it you have a WordPress site ready.
- But if you are more into development you most probably will have the wp-content folder's content already.

**From here you have two ways to go**

**Automated😎 -**

- Just make sure you have cloned the `wordpress.setup` repo in `~/wordpress/wordpress.setup-DO-NOT-DELETE`.
- And now there inside there you will find a script named `setup.sh`.
- Just run the script as so - `setup.sh app_name /path/where/the/proj/should/be/created wp-content_repo_url(optional)`.
- And your app is ready!

**Manual🧐 -**

- So, in a different folder copy the `.lando.yml`, `wp-content`(fallback), `.lando` files.
- And now you can get your's `wp-content` folder and replace this default `wp-content` folder.
- In the first line of `.lando.yml` file edit the `name` parameter. ( Important ).
- Now run `lando start`.
- Here only you will get a `wp-config.php` file which you can edit as per you wish.

## TO-DO:

- [x] Ability to add separate `wp-config.php` files for different sites.
- [x] Add a shell script to complete the setup following the above steps ( only contains basic level of error handling ).
- [ ] Add far better error handling in the shell script.
