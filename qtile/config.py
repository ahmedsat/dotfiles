# -*- coding: utf-8 -*-
import os
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag,Match, Screen
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy

from vars import *
from keys import *
from groups import *


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
]

widget_defaults = dict(
    font="Hack Bold",
    fontsize=10,
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

    widget.HDDBusyGraph(
        foreground=colors[1],
        fill_color=colors[1],
        background=colors[7],
        # fmt='Vol: {}',
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
              *powerLineWidgetsList(widgetsList),
            ],
            24, 
        ),
        
       # bottom=bar.Bar(
       #     [


       #         widget.Spacer(
       #             background=colors[0],
       #         ),
       #         widget.LaunchBar(

       #             default_icon='/usr/share/icons/Adwaita/256x256/mimetypes/x-package-repository.png',

       #            progs=[
       #                 # ('pcmanfm','pcmanfm','pcmanfm'),
       #             ],


       #             background=colors[0],
       #         ),

       #         widget.Prompt(
       #             foreground=colors[2],
       #             background=colors[0],
       #         ),

       #         widget.Spacer(
       #             background=colors[0],
       #         ),

       #     ],
       #     24, 
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
        Match(wm_class="app"),  # testing app
        Match(wm_class="Test"),  # testing app
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
    #home = os.path.expanduser('~/.config//autostart.sh')
    subprocess.call(["autostart.sh"])
