#!/usr/bin/env bash 

source $Home/.bashrc

setdate 

sxhkd &

picom &

volumeicon &

find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &

nala update 
