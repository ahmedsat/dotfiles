

export DOTFILES_PATH=$HOME/.local/share/dotfiles

PATH=/usr/local/bin:/usr/bin/:/bin:/usr/local/games/usr/games/:$HOME/.local/bin:$HOME/.local/go/bin/
PATH=$PATH:$DOTFILES_PATH/script:$DOTFILES_PATH/script/dmenu-script
export PATH

source $DOTFILES_PATH/terminal/aliases.sh
source ~/.top_secret

shopt -s autocd

export NVM_DIR="$HOME/.nvm"
export EDITOR=vim
export HISTCONTROL=ignoreboth
export TERM=alacritty
export VISUAL=codium
export BROWSER=brave-browser
export FILE_MANAGER=pcmanfm
export LESS='-M'
export CLICOLOR=1
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
export TERM=xterm-256color
export ANDROID_HOME=/usr/lib/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

PATH=/sbin:/usr/local/bin:/usr/bin/:/bin:/usr/local/games/usr/games/:$HOME/.local/bin:$HOME/.local/go/bin/:$HOME/.local/fultter/bin
PATH=$PATH:$DOTFILES_PATH/script:$DOTFILES_PATH/script/dmenu-script
PATH=$PATH:$HOME/.cargo/bin/
PATH=$PATH:~/.local/opt/odin
PATH=$PATH:~/.local/opt/Hubstaff
export PATH=$PATH:~/.pub-cache/bin
export PATH

export STARSHIP_CONFIG=$DOTFILES_PATH/starship.toml


Black='\e[0;30m';
Blue='\e[0;34m';
Green='\e[0;32m';
Cyan='\e[0;36m';
Red='\e[0;31m';
Purple='\e[0;35m';
Brown='\e[0;33m';

# starsip prompt
eval "$(starship init bash)"


complete -cf doas
# complete -F _command doas
. "$HOME/.cargo/env"


function yy() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

NPM_PACKAGES="${HOME}/.npm-packages"
export PATH="$PATH:$NPM_PACKAGES/bin"
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"

export QT_QPA_PLATFORM=wayland
export QT_QPA_PLATFORMTHEME=qt5ct

tesk list --page 1 --size 10


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

if [[ -z $DISPLAY ]] && [[ $(tty) = /dev/tty1 ]]; then
	# setdate
	exec start-hyprland
fi
