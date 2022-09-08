default:
	@echo "nothing"

ln:
	ln -sf $(pwd)/emacs ~/.config/emacs
	ln -sf $(pwd)/terminal ~/.config/terminal
	ln -sf $(pwd)/.bashrc ~/.bashrc
	ln -sf $(pwd)/fancyprompts ~/.config/fancyprompts
	ln -sf $(pwd)/qtile ~/.config/qtile

non:
	ln -sf $(pwd)/emacs ~/.emacs.d