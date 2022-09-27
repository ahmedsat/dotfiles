current_dir = $(shell pwd)

default:
	@echo "nothing"

ln:
	ln -sf $(current_dir)/emacs ~/.config/emacs
	ln -sf $(current_dir)/terminal ~/.config/terminal
	ln -sf $(current_dir)/.bashrc ~/.bashrc
	ln -sf $(current_dir)/.xprofile ~/.xprofile
	ln -sf $(current_dir)/fancyprompts ~/.config/fancyprompts
	ln -sf $(current_dir)/qtile ~/.config/qtile

non:
	ln -sf $(pwd)/emacs ~/.emacs.d
