#!/bin/sh

# /etc/X11/xinit/xinitrc
#
# global xinitrc file, used by all X sessions started by xinit (startx)

# invoke global X session script
#. /etc/X11/Xsession &

export DOTFILES_PATH=$HOME/.local/share/dotfiles

PATH=/usr/local/bin:/usr/bin/:/bin:/usr/local/games/usr/games/:$HOME/.local/bin:$HOME/.local/go/bin/:$HOME/.local/fultter/flutter/bin
PATH=$PATH:$DOTFILES_PATH/script:$DOTFILES_PATH/script/dmenu-script
export PATH

# make sure flutter work with linux
#export CPLUS_INCLUDE_PATH="${CPLUS_INCLUDE_PATH:+${CPLUS_INCLUDE_PATH}:}/usr/include/c++/12/"
#export CPLUS_INCLUDE_PATH="${CPLUS_INCLUDE_PATH:+${CPLUS_INCLUDE_PATH}:}/usr/include/x86_64-linux-gnu/c++/12/"
#export CMAKE_INSTALL_PREFIX="$HOME/.local/camke/"

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"

exec qtile start

