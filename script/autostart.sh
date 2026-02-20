#!/usr/bin/env bash 

source $Home/.bashrc

# setdate

# emacs --daemon &

nm-applet & waybar &

hyprpaper &

sxhkd &

lxpolkit &

blueman-applet &

# picom &

# volumeicon &

export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
# virtscreen &

mkdir -p $HOME/drive

# rclone mount --daemon work-drive: $HOME/drive &
# sync-drive &

find $DOTFILES_PATH/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"

