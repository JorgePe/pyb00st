#!/usr/bin/env python3

from other.pyboost.movehub import MoveHub
from other.pyboost.constants import *
from time import sleep

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")

for color in LED_COLORS:
    mymovehub.set_led_color(color)
    sleep(1)
