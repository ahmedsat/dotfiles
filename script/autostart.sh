#!/usr/bin/env bash 

source $Home/.bashrc

setdate 

sxhkd &

picom &

volumeicon &

find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"

