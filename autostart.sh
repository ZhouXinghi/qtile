#!/bin/bash 

# xmodmap ~/.xmodmap
xrandr --output HDMI-0 --left-of DP-2 --auto
picom --experimental-backends &


