from libqtile.config import KeyChord, Key
from libqtile.lazy import lazy
from vars import *

terminalKeys = [
    Key([], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([], "d", lazy.group["scratchpad"].dropdown_toggle("debug")),
    Key([], "l", lazy.group["scratchpad"].dropdown_toggle("log")),
    Key([], "s", lazy.group["scratchpad"].dropdown_toggle("scrcpy")),

]

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.reset()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    

    Key([mod],"Tab", lazy.layout.next()),
    Key([mod],"space", lazy.next_layout()),
    
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "c", lazy.window.kill()),
    Key([mod, "control"], "q", lazy.shutdown()),
    
    Key(["control", "shift"], "r", lazy.reload_config()),
    Key([mod, "control", "shift"], "r", lazy.restart()),
    Key([mod], "space",lazy.next_layout()),
    Key([alt],"Tab",lazy.widget["keyboardlayout"].next_keyboard()),

    Key([mod, "control", "shift"], "b", lazy.hide_show_bar("top")),
    Key([mod], "r", lazy.spawn("dmenu_run_history")),


    # terminal keys
    Key([mod], "Return",lazy.spawn(terminal)),
    KeyChord([mod], "t", terminalKeys),

]
