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
    layout.MonadTall(
        align=layout.MonadTall._left,
        border_focus="#ff5e00",
        border_normal="#00a1ff",
        change_ratio=0.05,
        max_ratio=0.75,
        min_ratio=0.25,
        min_secondary_size=85,
        new_client_position='after_current',
        ratio=0.70,
        border_width=1,
        margin=10,
        single_border_width=0,
        single_margin=0,
    ),
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
        update_interval=60,
        distro="Debian",
        display_format="Updates: {updates} ",
        no_update_string='No updates',
        foreground=colors[1],
        colour_have_updates=colors[1],
        colour_no_updates=colors[1],
        mouse_callbacks={
            'Button3': lambda: qtile.cmd_spawn(terminal + ' -e doas nala upgrade'),
            'Button1': lambda: qtile.cmd_spawn(terminal + ' -e doas nala update')
            },
        padding=5,
        background=colors[3]
    ),

    widget.GenPollCommand(
        background=colors[4],
        foreground=colors[1],
        cmd = 'vrsc',
        update_interval=3600,
    ),

    # widget.HDDBusyGraph(
    #     foreground=colors[1],
    #     fill_color=colors[1],
    #     background=colors[7],
    #     padding=5,
    # ),


    widget.KeyboardLayout(
        configured_keyboards=['us','eg'],
        foreground=colors[1],
        background=colors[8],
    ),

    widget.Battery(
        foreground=colors[1],
        fill_color=colors[1],
        background=colors[7],
        padding=5,
        update_interval=1,
        # charge_controller: lambda (0, 90),
    ),

     widget.Systray(
        icon_size=18,
        foreground=colors[1],
        background=colors[2],
        padding=5,
    ),

     widget.BatteryIcon(
        foreground=colors[1],
        background=colors[2],
        fill_color=colors[1],
        update_interval=1,
        # charge_controller: lambda (0, 90)
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
                os.getenv("DOTFILES_PATH")+"/icons")],
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
    list = []
    # arrow_widget=None
    arrow_widget = widget.TextBox(
        text=arrow,
        background=previous_color,
        foreground=background,
        fontsize=28,
        padding=-1,
    )

    # if widgetToRender.name !="Battery":
    list.append(arrow_widget)
    list.append(widgetToRender)

    return list


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
            18,
        ),

    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", 
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(
        [mod], "Button3", 
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click(
        [mod], "Button2", 
        lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
	Match(wm_class="erp-reports"), #
	Match(wm_class="Test"),  # testing app
        Match(title="Test"),  # testing app
        Match(wm_class="examples"),  # testing app
        Match(wm_class="app"),  # testing app
        Match(wm_class=""),  # testing app
        Match(wm_class=""),  # testing app
        Match(wm_class="naf3"),  # naf3
        Match(wm_class="LearnOpenGL"),  # testing app
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True

focus_on_window_activation = "smart"

reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    subprocess.call(["autostart.sh"])
