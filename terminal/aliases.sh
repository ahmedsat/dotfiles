#-------------------------------------------------------------------------
# Copyright (C) 2022 AhmedSat
#-------------------------------------------------------------------------

# my aliases

alias search='nala search'
alias show="nala show"
alias update='doas nala update'
alias upgrade='doas nala upgrade '
alias clean='doas nala clean'
alias install='doas nala install'
alias history='nala history'
alias undo='doas nala history'
alias list='nala list --upgradable'
alias purge='doas nala purge'
alias remove='doas nala remove'
alias autopurge='doas nala autopurge'

alias emacs='emacsclient --create-frame --alternate-editor=""'

alias reload='source ~/.bashrc' # reload .bashrc file


alias x=startx

alias c='clear'

alias ls='ls --color=auto'
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
