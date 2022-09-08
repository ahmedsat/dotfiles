;; Move customization variables to a separate file and load it
(setq custom-file (locate-user-emacs-file "custom-vars.el"))
(load custom-file 'noerror 'nomessage)

(setq inhibit-startup-message t ; don't show welcome screen
      history-length 25 ; max command to remember
      use-dialog-box nil ; Don't pop up UI dialogs when prompting
      )

(tool-bar-mode -1) ; hide tool bar
(menu-bar-mode -1) ; hide menu bar
(scroll-bar-mode -1) ; hide scroll bar
(global-display-line-numbers-mode 1) ; show line numbers
(recentf-mode 1) ; remember recent file opend 
(hl-line-mode 1) ; highlight current line
(savehist-mode 1) ; save excuted commands
(save-place-mode 1) ; remember and restore last cursor location of opent file
(global-auto-revert-mode 1) ; Revert buffers when the underlying file has changed

(load-theme 'modus-vivendi t) ; set color theme



;; (bind-key* "C-M-x" eval-defun)

