#!/usr/bin/env python3

from pyb00st import MoveHub
from pyb00st.constants import *
from time import sleep

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")

for color in LED_COLORS:
    mymovehub.set_led_color(color)
    sleep(1)
