#-------------------------------------------------------------------------
# Copyright (C) 2022 AhmedSat
#-------------------------------------------------------------------------

# my aliases

alias search='nala search'
alias show="nala show"
alias update='sudo nala update'
alias upgrade='sudo nala upgrade '
alias clean='sudo nala clean'
alias install='sudo nala install'
alias history='nala history'
alias undo='sudo nala history'
alias list='nala list --upgradable'
alias purge='sudo nala purge'
alias remove='sudo nala remove'
alias autopurge='sudo nala autopurge'

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

alias setdate='sudo ntpdate ntp.ubuntu.com'

alias :wq=exit
