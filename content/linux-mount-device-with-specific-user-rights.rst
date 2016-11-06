 Mount device with specific user rights
#######################################
:date: 2015-06-03 16:11
:author: aidanharris
:category: Linux
:slug: linux-mount-device-with-specific-user-rights
:status: published

Recently I bought myself a `Raspberry Pi
2 <https://en.wikipedia.org/wiki/Raspberry_Pi>`__. One of the first
things I wanted to do was to install `Kodi <https://kodi.tv>`__. This
was easy enough thanks to the apt package manager included with
`Rasbian <https://www.raspbian.org>`__. It's as simple as
``sudo apt-get install kodi``.

However since the Kodi user data and cache can grow quite large I
decided to place the .kodi folder on a USB drive. This was as simple as
copying the ``.kodi`` folder from ``~/.kodi`` to my USB drive mounted at
/mnt/USB and creating a symlink in ``/home/pi`` to the USB using
``ln -s /mnt/USB/.kodi /home/pi/.kodi``.

The above worked no problem at all however I quickly ran into problems
because by default my USB drive was mounted as root. Sure I could
``chmod 777`` the entire directories but this didn't seem like the best
way to go about things. A quick search online took me to the following
`SuperUser
post <https://superuser.com/questions/320415/linux-mount-device-with-specific-user-rights>`__.
Within this post there was a nice one liner that allowed me to mount the
USB with the user pi.

::

    mount -t deviceFileFormat -o umask=filePermissons,gid=ownerGroupID,uid=ownerID /device /mountpoint

I simply had to use the ``id`` command to find the uid and guid of the
user pi (``id pi``) and then place the command in ``/etc/rc.local`` to
mount the device on boot, although I should probably move it to
``/etc/fstab``.
