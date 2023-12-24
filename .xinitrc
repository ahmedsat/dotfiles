#!/bin/sh

# /etc/X11/xinit/xinitrc
#
# global xinitrc file, used by all X sessions started by xinit (startx)

# invoke global X session script
#. /etc/X11/Xsession &


# make sure flutter work with linux
export CPLUS_INCLUDE_PATH="${CPLUS_INCLUDE_PATH:+${CPLUS_INCLUDE_PATH}:}/usr/include/c++/12/"
export CPLUS_INCLUDE_PATH="${CPLUS_INCLUDE_PATH:+${CPLUS_INCLUDE_PATH}:}/usr/include/x86_64-linux-gnu/c++/12/"
export CMAKE_INSTALL_PREFIX="$HOME/.local/camke/"

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"

exec qtile start
