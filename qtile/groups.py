from libqtile.config import Group,  Key, ScratchPad,DropDown

from vars import *
from keys import *

groups = [
    Group("WWW"),
    Group("DEV"),
    Group("SYS"),
    Group("FILE"),
    Group("OTHER"),
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term", 
                terminal + " -t terminal", 
                opacity=1.0,x=0.05, y=0.05, 
                width=0.9, 
                height=0.9, 
                on_focus_lost_hide=False),
            DropDown(
                "debug", 
                terminal + " -t debug", 
                opacity=1.0,
                x=0.05, 
                y=0.05, 
                width=0.9, 
                height=0.9, 
                on_focus_lost_hide=False),
            DropDown(
                "log", 
                terminal + " -t log -e htop", 
                opacity=1.0,
                x=0.05, 
                y=0.05, 
                width=0.9, 
                height=0.9, 
                on_focus_lost_hide=False),
            DropDown(
                "scrcpy", 
                "scrcpy", 
                opacity=1.0,
                x=0.3625, 
                y=-0.0225, 
                width=0.275, 
                height=1.0225, 
                on_focus_lost_hide=False),
        ]),
]

groups_keys = {
    "w": groups[0],
    "d": groups[1],
    "s": groups[2],
    "f": groups[3],
    "o": groups[4],
}

for k, g in groups_keys.items():
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc="Switch to group {}".format(g.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    k,
            #    lazy.window.togroup(g.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(
            #        g.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
             Key(
                 [mod, "shift"], 
                 k, 
                 lazy.window.togroup(g.name),
                 desc="move focused window to group {}".format(g.name),
            ),
        ]
    )
