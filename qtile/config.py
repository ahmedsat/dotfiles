# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# mod keys
mod = "mod4"
alt = "mod1"
shift = "shift"
space = "space"
ctrl = "control"

if qtile.core.name == "x11":
    mod = "mod4"
elif qtile.core.name == "wayland":
    mod = "mod1"

# terminal = guess_terminal()
terminal = "alacritty"
fileManger = "pcmanfm"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # my custom key bindings
    Key(["control", "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([ctrl], "f", lazy.spawn(fileManger), desc="Lunch file manager"),
    # Key([mod], "e", lazy.spawn("emacsclient -c"), desc="Lunch emacs client"),
    # Key([mod], "m", lazy.spawn("emacs --with-profile=satmacs"), desc="Lunch emacs"),

    # key([crtl,shift],"p", lazy.spawn("sudo systemctl poweroff"), desc="Shutdown PC"),

    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
]


groups = [
    Group("WWW"),
    Group("DEV"),
    Group("SYS"),
    Group("FILE"),
    Group("OTHER"),
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
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    g.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    #  layout.TreeTab(
    #      fontsize=10,
    #      sections=["OPENED TAPS"],
    #      section_fontsize=10,
    #      border_width=2,
    #      bg_color="1c1f24",
    #     active_bg="c678dd",
    #      active_fg="000000",
    #      inactive_bg="a9a1e1",
    #      inactive_fg="1c1f24",
    #      padding_left=0,
    #      padding_x=0,
    #      padding_y=5,
    #      section_top=10,
    #      section_bottom=20,
    #      level_shift=8,
    #      vspace=3,
    #      panel_width=150
    #  ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.floating(),
]


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#da8548", "#da8548"],
          ["#a9a1e1", "#a9a1e1"],
          ["#c678dd", "#c678dd"],
          ["#98be65", "#98be65"],
          ["#51afef", "#51afef"],
          ["#46d9ff", "#46d9ff"],
          ["#ff6c6b", "#ff6c6b"],
          ]

arrow = ''


widget_defaults = dict(
    # font="sans",
    # fontsize=12,
    # padding=3,
    font="Hack Bold",
    fontsize=10,
    # padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

widgetsList = [
    widget.CheckUpdates(
        update_interval=1800,
        distro="Debian",
        display_format="Updates: {updates} ",
        foreground=colors[1],
        colour_have_updates=colors[1],
        colour_no_updates=colors[1],
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
            terminal + ' -e sudo nala upgrade')},
        padding=5,
        background=colors[3]
    ),

    widget.Volume(
        foreground=colors[1],
        background=colors[7],
        fmt='Vol: {}',
        # emoji=True,
        padding=5,
    ),
    widget.KeyboardLayout(
        configured_keyboards=['us', 'ar'],
        foreground=colors[1],
        background=colors[8],
    ),

     widget.Systray(
        icon_size=20,
        foreground=colors[1],
        padding=5,
        background=colors[2]
    ),

    widget.Clock(
        fontsize=18,
        format="%H:%M",
        foreground=colors[1],
        background=colors[9],
    ),
]


def currentLayouts():
    return [
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser(
                "~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
        ),
    ]


# def systray():
#     return [
#         widget.Sep(
#             linewidth=0,
#             padding=6,
#             foreground=colors[0],
#             background=colors[7]
#         ),
#         widget.Systray(
#             icon_size=500,
#             background=colors[1],
#             padding=5
#         ),
#         widget.Sep(
#             linewidth=0,
#             padding=6,
#             foreground=colors[0],
#             background=colors[7]
#         ),
#     ]


def powerLineWidget(widgetToRender, background, foreground, previous_color):
    widgetToRender.background = background
    widgetToRender.foreground = foreground
    arrow_widget = widget.TextBox(
        text=arrow,
        # font="Ubuntu Mono",
        background=previous_color,
        foreground=background,
        fontsize=28,
        padding=-1,
    )
    return [
        arrow_widget,
        widgetToRender,
    ]


def powerLineWidgetsList(WidgetsList):
    list = []
    previous_color = colors[0]
    for w in widgetsList:
        list.extend(powerLineWidget(w,
                    w.background, w.foreground, previous_color))
        previous_color = w.background
    return list


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    foreground=colors[2],
                    background=colors[0]
                ),
                widget.GroupBox(
                    font="Ubuntu Bold",
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=3,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[7],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[6],
                    other_screen_border=colors[4],
                    foreground=colors[2],
                    background=colors[0]
                ),
                *currentLayouts(),

                widget.Prompt(
                    foreground=colors[2],
                    background=colors[0],
                ),
                widget.WindowName(
                    foreground=colors[6],
                    background=colors[0],
                    padding=0
                ),
            #    *systray(),

              *powerLineWidgetsList(widgetsList),

            ],
            24, ),
        # bottom=bar.Bar(
        #     [
        #         widget.Prompt(),
        #         # widget.Chord(
        #         #     width=bar.CALCULATED,
        #         #     chords_colors={
        #         #         "launch": ("#ff0000", "#ffffff"),
        #         #     },
        #         #     name_transform=lambda name: name.upper(),
        #         # ),
        #         # widget.TextBox("default config", name="default"),
        #         # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        #         # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        #         # widget.StatusNotifier(),
        #         # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        #         # PowerlineTextBox(update_interval=2, side='left'),
        #         # Spacer(),
        #         # PowerlineTextBox(update_interval=2, side='right'),
        #         widget.CPUGraph(),
        #         # widget.CheckUpdates(
        #         #     background='#6272a4',
        #         #     colour_have_updates='ffffff',
        #         #     colour_no_updates='ffffff',
        #         #     display_format='Updates: {updates}',
        #         #     distro="Debian",
        #         #     # execute='tilix -e sudo nala upgrade',
        #         #     foreground='#8be9fd',
        #         #     no_update_string='None',
        #         #     padding=4,
        #         #     update_interval=60,),
        #         # widget.Clock(format="%H:%M"),

        #         widget.QuickExit(),
        #     ],
        #     24,
        #     # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        #     # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
