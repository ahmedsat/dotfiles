#!/usr/bin/env bash 

# nitrogen --restore &

go-clip serve &
go-clip serve -a "/tmp/queue.sock" &

sxhkd &
picom &
conky -c $HOME/.config/conky/conkyrc
conky -c $HOME/.config/conky/tasklist.conf
volumeicon &
find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &
killall x-terminal-emulator &
killall xterm &
