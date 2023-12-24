
;; add melpa repo
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)


(setq inhibit-startup-message t)
(menu-bar-mode 0)
(tool-bar-mode 0)

(add-to-list 'default-frame-alist
             '(font . "Hack Nerd Font Mono-12"))

(custom-set-variables '(custom-enabled-themes '(modus-vivendi)))
(custom-set-faces )
