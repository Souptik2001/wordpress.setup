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
- So, just where you have `wp-content` folder's content run copy this `.lando.yml` file and run `lando start` and that's it. DONE!

## TO-DO:

[ ] Ability to add separate `wp-config.php` files for different sites.