<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'wordpress' );

/** Database password */
define( 'DB_PASSWORD', 'wordpress' );

/** Database hostname */
define( 'DB_HOST', 'database' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          'Pyn C*iYkQ/Mc^wTc!CB;To5HCK5]B|euhFteOgpgh0fNU^[8NQ~Di20kb0;9ccM' );
define( 'SECURE_AUTH_KEY',   'LC2|m$vLbTqav)Jwsv3b-@,eD:B4SZX p uLgql,nRN tD<FeT5$O9F&QaBn [];' );
define( 'LOGGED_IN_KEY',     'p%UTs=s5<3Kvy2<+;rSGCLsrOJJ=^?8_zV*9@`[zeP^I(((tr@Z >nQIXn/@Z?BK' );
define( 'NONCE_KEY',         '$<EhVFTJ-@9jxr:{^p2K09_cP+g!o$F;!E!~*tnjscw<u[Hmw@%(LN^&B3_;)5_Y' );
define( 'AUTH_SALT',         'd_Utg6;rF%9 h7;#S@kdar$tGB/7irvaPT /KUU4@0F,=s Q:2dUq84Hsp;JO|:I' );
define( 'SECURE_AUTH_SALT',  '_o&Foqd0)!a}jbKs~kph PB(a:[2iQ,wGE}$,d?z$q,t1}_d4(Xx/[Ve3qq5KA?X' );
define( 'LOGGED_IN_SALT',    'mqmn{1~ERSa:it)3Ph50IVWJt.,rqV,)}5?*8qdPj0wWm<X8=j-6a)dtmro;=$5;' );
define( 'NONCE_SALT',        'Z@Uji!4,uJjfZAgL}$y]1-)jPr:0z$ZxVXDzk]#rq&P:?QXTXR{FjNBm^Fya]eCY' );
define( 'WP_CACHE_KEY_SALT', 'RSe_.lR6e9&Rg:ZCN2[3e&vi<)Gv@s6q];+FKq2G_.hWk:,6D|{J_agx`Q^|PDQ)' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', true );


/* Add any custom values between this line and the "stop editing" line. */

$redis_server = array(
    'host'     => 'rediscache',
    'port'     => 6379,
);


define( 'WP_DEBUG_LOG', true );
define( 'WP_DEBUG_DISPLAY', true );
define( 'AUTOMATIC_UPDATER_DISABLED', true );
define( 'DISALLOW_FILE_EDIT', false );
define( 'WP_ENVIRONMENT_TYPE', 'local' );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
