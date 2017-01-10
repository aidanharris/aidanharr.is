 Change Wordpress theme depending on visitor IP address
#######################################################
:id: 3
:date: 2015-10-11 18:46
:author: aidanharris
:category: PHP, Programming, Wordpress
:slug: change-wordpress-theme-depending-on-visitor-ip-address
:status: published
:headingIconFont: fa fa-wordpress

Developing and testing in production is a terrible, terrible idea.
However until I set up a virtual machine development environment I have
little choice but to do so. Here's how to change the theme depending on
the user's IP address:

Create a new plugin (you might want to use the following directory
structure):

.. code-block:: bash

    wordpress
    └── wp-content
        └── plugins
            └── change-theme-by-ip-address
                └── change-theme-by-ip-address.php

Inside your plugin add the following code:

.. code-block:: php

    <?php
    /*
    Plugin Name: change-theme-by-ip-address
    Description: Changes the Wordpress theme depending on the visitor's IP address
    */
    function fxn_change_theme($theme) {
        $IPADDRESS = "";
        // If your website is using CloudFlare you need to use the $_SERVER["HTTP_CF_CONNECTING_IP"] variable
        if(isset($_SERVER["HTTP_CF_CONNECTING_IP"])) {
            $IPADDRESS = $_SERVER["HTTP_CF_CONNECTING_IP"];
        } else {
            $IPADDRESS = $_SERVER['REMOTE_ADDR'];
        }
        // Change 127.0.0.1 to your public IP address
        if( "$IPADDRESS" == "127.0.0.1" )
            $theme = 'your-theme-dev';
        else
            $theme = 'your-theme';
        return $theme;
    }

    add_filter('template', 'fxn_change_theme');
    add_filter('option_template', 'fxn_change_theme');
    add_filter('option_stylesheet', 'fxn_change_theme');
    ?>

Enable the plugin and you should notice your theme changes for your IP
address while at the same time everybody else has the old theme. This
allows you to safely make changes to your theme in production (although
it's still worth setting up a virtual machine for development in order
to ensure nothing goes wrong and if something does go wrong then no big
deal just restore the virtual machine from a snapshot).
