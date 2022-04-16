# My WordPress Lando Setup ~ Souptik Datta

## Steps to set-up:

- Clone this repo(preferably in your home directory) using the command:
```bash
git clone https://github.com/Souptik2001/wordpress.setup.git wordpress.setup-DO-NOT-DELETE
```
OR
```bash
git clone git@github.com:Souptik2001/wordpress.setup.git wordpress.setup-DO-NOT-DELETE
```
- Now you can just run `lando start` here only and that's it you have a WordPress site ready.
- But if you are more into development you most probably will have the wp-content folder's content already.
- So, in a different folder copy the `.lando.yml`, `wp-content`(fallback), `.lando` files.
- And now you can get your's `wp-content` folder and replace this default `wp-content` folder.
- Now run `lando start`.
- Here only you will get a `wp-config.php` file which you can edit as per you wish.

## TO-DO:

- [x] Ability to add separate `wp-config.php` files for different sites.
- [ ] Add a shell script to complete the setup following the above steps.