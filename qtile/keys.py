from libqtile.config import KeyChord, Key
from libqtile.lazy import lazy
from vars import *

terminalKeys = [
    Key([], "Return", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, shift], "g", lazy.group["scratchpad"].dropdown_toggle("debug")),
]

emacsKeys = [
    Key([], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Emacsclient Dashboard"),
    Key(
        [],
        "a",
        lazy.spawn(
            "emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"
        ),
        desc="Emacsclient EMMS (music)",
    ),
    Key(
        [],
        "b",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
        desc="Emacsclient Ibuffer",
    ),
    Key(
        [],
        "d",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
        desc="Emacsclient Dired",
    ),
    Key(
        [],
        "i",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
        desc="Emacsclient ERC (IRC)",
    ),
    Key(
        [],
        "n",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
        desc="Emacsclient Elfeed (RSS)",
    ),
    Key(
        [],
        "s",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
        desc="Emacsclient Eshell",
    ),
    Key(
        [],
        "v",
        lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
        desc="Emacsclient Vterm",
    ),
    Key(
        [],
        "w",
        lazy.spawn(
            "emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"
        ),
        desc="Emacsclient EWW Browser",
    ),
]

systemKeys = [
    Key(
        [],
        "w",
        lazy.spawn(
            "find $HOME/dotfiles/wallpaper/ -type f | shuf -n 1 | xargs xwallpaper --zoom"
        ),
    ),
]

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # my custom key bindings
    Key(["control", "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "r", lazy.restart(), desc="Restart qtile"),
    # Key([ctrl], "f", lazy.spawn(fileManger), desc="Lunch file manager"),
    # Key([mod], "e", lazy.spawn("emacsclient -c"), desc="Lunch emacs client"),
    # Key([mod], "m", lazy.spawn("emacs --with-profile=satmacs"), desc="Lunch emacs"),
    # key([crtl,shift],"p", lazy.spawn("sudo systemctl poweroff"), desc="Shutdown PC"),
    Key(
        [alt],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    KeyChord([mod], "Return", terminalKeys),
    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    # KeyChord([mod], "e", emacsKeys),
    # KeyChord([ctrl,shift], "s", systemKeys),
]
