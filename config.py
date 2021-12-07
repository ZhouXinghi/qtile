# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown

from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import KeyChord
#  from libqtile.backend.base import Window

mod = "mod1"
#  terminal = guess_terminal()
terminal = "st"

keys = [
    #  Key([mod], "`", lazy.group['scratchpad'].dropdown_toggle('term')),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "s", lazy.next_screen()),
    Key([mod, "control"], "h", lazy.hide_show_bar("all")),
    #  Key([mod], "r", lazy.reload_config(),
    #  KeyChord([mod], "o", [
    #      Key([], "j", lazy.down_opacity()),
    #      Key([], "k", lazy.up_opacity())],
    #  mode = "opacity"
    #  )
    
    #  Key([mod], "w", lazy.to_screen(0)),
    #  Key([mod], "e", lazy.to_screen(1)),
    #  Key([mod], "space", lazy.layout.next(),
    #      desc="Move window focus to other window"),

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "o", lazy.window.opacity(1.0)),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], 'd', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="monaco",
    ))),

    #  Key([mod], 'm', lazy.run_extension(extension.CommandSet(
    #     commands={
    #         'play/pause': '[ $(mocp -i | wc -l) -lt 2 ] && mocp -p || mocp -G',
    #         'next': 'mocp -f',
    #         'previous': 'mocp -r',
    #         'quit': 'mocp -x',
    #         'open': 'urxvt -e mocp',
    #         'shuffle': 'mocp -t shuffle',
    #         'repeat': 'mocp -t repeat',
    #         },
    #     pre_commands=['[ $(mocp -i | wc -l) -lt 1 ] && mocp -S'],
    #  **Theme.dmenu))),   ),




    # increase/decrease the space for window
    # Key([mod], "n", lazy.layout.increase_ratio(), desc="increase size"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "g", lazy.spawn("google-chrome-stable"), desc="Launch chrome"),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 2+ unmute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 2- unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #  Key([mod], "r", lazy.spawncmd(),
    #      desc="Spawn a command using a prompt widget"),

]

#  groups = [Group(i) for i in "123456789"]
#  groups = [
#          ScratchPad("scratchpad", [
#          # define a drop down terminal.
#          # it is placed in the upper third of screen by default.
#          DropDown("term", "urxvt", opacity=0.8),
#
#          # define another terminal exclusively for ``qtile shell` at different position
#          DropDown("qtile shell", "urxvt -hold -e 'qtile shell'",
#                   x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
#                   on_focus_lost_hide=True) ]),
#          Group("a"),
#  ]
#  groups = ["1", "2", "3", "4", "5", "6"]
groups = [
        Group("ter1"),
        Group("ter2"),
        Group("ter3", spawn = "st"),
        Group("bro4"),
        Group("bro5"),
        Group("6"),
        Group("7"),
        Group("mai8", spawn = "st"),
        Group("9"),
]
groups.append(
        ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
            DropDown("term", terminal, opacity=0.8),

            # define another terminal exclusively for ``qtile shell` at different position
            DropDown("qtile shell", "st -hold -e 'qtile shell'",
                 x=0.05, y=0.4, width=0.9, height=0.6, opacity=0.9,
                 on_focus_lost_hide=True) 
        ])
)

for i in range(len(groups) - 1):
    group = groups[i]
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i + 1), lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        #  Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #      desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], str(i + 1), lazy.window.togroup(group.name)),
    ])

def init_layout_theme():
    return { "border_width": 2,
            "margin": [10, 5, 10, 5],
            "border_focus": "#AD69AF",
            "border_normal": "#000000"
            }

layout_theme = init_layout_theme()
layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    #  layout.Max(),
    # Try more layouts by unleashing below layouts.
    #  layout.Stack(num_stacks=4),
    # layout.Bsp(),
    # layout.Matrix(),
    #  layout.MonadTall(
    #      border_width = 2,
    #      margin=10,
    #      border_focus="AD69AF",
    #      border_normal = "1D2330"
    #      ),
    #  layout.MonadTall(),
    # layout.MonadWide(),
    #  layout.RatioTile(),
    layout.Tile(ratio = 0.618, **layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(linewidth = 0, padding = 6),
                widget.DF(warn_space = 10),
                #  widget.CurrentLayout(padding = 10),
                widget.CurrentLayoutIcon(),
                widget.CurrentScreen(),
                widget.GroupBox(hide_unused = True, highlight_method = 'block'),
                #  widget.Prompt(),
                #  widget.WindowName(),
                widget.TaskList(highlight_method = 'block'),
                #  widget.Backlight(),
                #  widget.BatteryIcon(),
                #  widget.Battery(),
                #  widget.Bluetooth(),
                widget.CPU(),
                widget.Sep(),
                widget.Memory(),
                #  widget.Clipboard(),
                #  wedget.Wlan(interface = 'wlan0'),
                #  widget.MemoryGraph(),
                widget.Sep(),
                widget.Net(interface = "wlp0s20f3"),
                widget.Sep(),
                widget.Net(interface = "enp60s0"),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #  widget.TextBox("default config", name="default"),
                #  widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Sep(),
                widget.Volume(),
                widget.Systray(),
                widget.CheckUpdates(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
                widget.Sep(linewidth = 0, padding = 6),
            ],
            24,
            background='#00000000',
        ),

        wallpaper="~/Pictures/Wallpapers/01.jpg",
        wallpaper_mode='fill',
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(linewidth = 0, padding = 6),
                widget.DF(warn_space = 10),
                #  widget.CurrentLayout(padding = 10),
                widget.CurrentLayoutIcon(),
                widget.CurrentScreen(),
                widget.GroupBox(hide_unused = True, highlight_method = 'block'),
                #  widget.Prompt(),
                #  widget.WindowName(),
                widget.TaskList(highlight_method = 'block'),
                #  widget.Backlight(),
                #  widget.BatteryIcon(),
                #  widget.Battery(),
                #  widget.Bluetooth(),
                widget.CPU(),
                widget.Sep(),
                widget.Memory(),
                #  widget.Clipboard(),
                #  wedget.Wlan(interface = 'wlan0'),
                #  widget.MemoryGraph(),
                widget.Sep(),
                widget.Net(interface = "wlp0s20f3"),
                widget.Sep(),
                widget.Net(interface = "enp60s0"),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #  widget.TextBox("default config", name="default"),
                #  widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Sep(),
                widget.PulseVolume(emoji = True),
                widget.Systray(),
                widget.CheckUpdates(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
                widget.Sep(linewidth = 0, padding = 6),
            ],
            24,
            background='#00000000',
        ),
        wallpaper="~/Pictures/Wallpapers/01.jpg",
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


import os
import subprocess

@hook.subscribe.startup_once
def autostart():  
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
