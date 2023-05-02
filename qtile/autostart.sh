#!/usr/bin/env bash 

# nitrogen --restore &

sleep 1

go-clip serve &
go-clip serve -a "/tmp/queue.sock" &

sxhkd &
picom &
conky -c $HOME/.config/conky/conkyrc
volumeicon &
find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom &
killall x-terminal-emulator &
killall xterm &
