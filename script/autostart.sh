#!/usr/bin/env bash 

source $Home/.bashrc

# setdate 

nm-tray &

emacs --daemon &

sxhkd &

picom &

volumeicon &

find $DOTFILES_PATH/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"

