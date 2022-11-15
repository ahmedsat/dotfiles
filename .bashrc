source ~/.config/terminal/aliases.sh

shopt -s autocd


# set CapsLock key to work as Ctrl
/usr/bin/setxkbmap -option "ctrl:nocaps"


export NVM_DIR="$HOME/.nvm"
export EDITOR=vim
export HISTCONTROL=ignoreboth
export TERM=xterm-256color
export VISUAL=vim
export LESS='-M'
export CLICOLOR=1
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
export PATH

Black='\e[0;30m';
Blue='\e[0;34m';
Green='\e[0;32m';
Cyan='\e[0;36m';
Red='\e[0;31m';
Purple='\e[0;35m';
Brown='\e[0;33m';

LAMDA='λ  '

ENDCOLOR="\e[0m"
PS1="$Green \w $LAMDA $ENDCOLOR"

PS1="$PS1"'\[\e[0m\]' # reset all
