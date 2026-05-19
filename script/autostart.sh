#!/usr/bin/env bash 

source "$HOME/.bashrc"

# setdate

# emacs --daemon &

nm-applet & waybar &

/home/ahmedsat/.local/share/dotfiles/script/hyprpaper-random &

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

# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"
