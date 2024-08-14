#-------------------------------------------------------------------------
# Copyright (C) 2022 AhmedSat
#-------------------------------------------------------------------------

# my aliases

pkm=nala

alias search='$pkm search'
alias show="$pkm show"
alias update='doas $pkm update'
alias upgrade='doas $pkm upgrade '
alias clean='doas $pkm clean'
alias install='doas $pkm install'
alias history='$pkm history'
alias undo='doas $pkm history'
alias list='$pkm list --upgradable'
alias purge='doas $pkm purge'
alias remove='doas $pkm remove'
alias autopurge='doas $pkm autopurge'

alias reload='source ~/.bashrc' # reload .bashrc file

alias x=startx

alias c='clear'

alias ls='ls --color=auto -h'
alias la='ls -A'
alias l='ls -CF'
alias ll='ls -alF'

alias r='fc -s'
alias vi='vim'

alias mv='mv -i'
# alias rm='rm -i'
alias cp='cp -i'
alias grep='grep --color=auto'
alias ..='cd ..'


# git aliases
alias gs='git status'
alias ga='git add'
alias gaa='git add --no-ignore-removal'
alias gc='git commit -m'
alias gp='git push'
gu(){
	git add --no-ignore-removal
	git commit -m "$1"
	git push
}

copy(){
	echo $1 | xclip -i -selection clipboard
}

dwmDate(){
	while true ; do now | xargs xsetroot -name ; sleep 1 ; done
}

alias setdate='doas ntpdate ntp.ubuntu.com'

alias :wq=exit

alias dc='pwd | xclip -i'

now(){
	date +'%Y/%m/%d-%H:%M:%S'
}

pipx='doas pipx'

alias pip=pipx
alias pip3=pipx
