source ~/dotfiles/terminal/aliases.sh
source ~/.top_secret

shopt -s autocd

export NVM_DIR="$HOME/.nvm"
export EDITOR=vim
export HISTCONTROL=ignoreboth
export TERM=alacritty
export VISUAL=code
export BROWSER=qutebrowser
export FILE_MANAGER=pcmanfm
export LESS='-M'
export CLICOLOR=1
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

DOTFILES_PATH=$HOME/dotfiles

PATH=/usr/local/bin:/usr/bin/:/bin:/usr/local/games/usr/games/:$HOME/.local/bin:$HOME/.local/go/bin/:$HOME/.local/fultter/flutter/bin
PATH=$PATH:$DOTFILES_PATH/script:$DOTFILES_PATH/script/dmenu-script
export PATH

export STARSHIP_CONFIG=$DOTFILES_PATH/starship.toml

# export MESA_GL_VERSION_OVERRIDE=4.5
export LIBGL_ALWAYS_SOFTWARE=1 # Fix error alacritty requires hardware supporting GLSL 3.30  

Black='\e[0;30m';
Blue='\e[0;34m';
Green='\e[0;32m';
Cyan='\e[0;36m';
Red='\e[0;31m';
Purple='\e[0;35m';
Brown='\e[0;33m';

# starsip prompt
eval "$(starship init bash)"

if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
	setdate
	exec startx
fi

