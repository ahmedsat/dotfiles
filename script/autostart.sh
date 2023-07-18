#!/usr/bin/env bash 

sxhkd &

picom &

volumeicon &

find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &

