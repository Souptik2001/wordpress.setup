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
define( 'AUTH_KEY',          '|x_SOMdW2C-zq`LaLx;W_8y[AB^eAkK6<PAZ jiz_4te/@!{KI:Y*s:q27*&FT5m' );
define( 'SECURE_AUTH_KEY',   'Sm],wR!n_Tgt?p(-61+B=;:nHPk%7]1/n:z6MduqA`e^>pQ;BKAskkmkhfgHLN8$' );
define( 'LOGGED_IN_KEY',     '_n}W=vdK(0*tEVKBZe xS~`Q/FU&#i F|d6O7@b*rt>Wm9` B0Y6^r/4la.F|NNV' );
define( 'NONCE_KEY',         'Wh ~=DSEdugC[w07r,aX}MW|cuP9(_ND_YX!:4bIq+_=cY|~XOx#Gt&>_1UiT.%9' );
define( 'AUTH_SALT',         'QH<Z&fgXD0_FtmM0Ax:g@Obu.5{E#Sk,_CxbjBi~r-(k#4n3pAvysx!`Q[@*nA8>' );
define( 'SECURE_AUTH_SALT',  ')uu?bW%@_q Yj:(c}GU(n?RDtm.1c)}AzEkR:o@q&d7sma7]0EQ_paYcL-SbV>xR' );
define( 'LOGGED_IN_SALT',    '+:C^>RX]`FVo2GKRHx%6l`.}?VK<&cuiKwon?.b1$PND<}7(4O%60QzuNC%P0<Ep' );
define( 'NONCE_SALT',        '0p:oiuw`?4MIM;@][xqr3ieR:vCgwtVz~_HAt|hR%IJU<ge?ow&k9GPd)5KS1=p]' );
define( 'WP_CACHE_KEY_SALT', '2ea8>>;=0FFno $22Fo Zji5IRSpKpFK*MZ!IRcqCfL:3_Y#:yQR[k#jTxXe@|DP' );


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
