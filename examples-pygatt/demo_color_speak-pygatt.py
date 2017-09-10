#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from espeak import espeak # apt install python3-espeak
from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

espeak.set_voice='en'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_color()
mymovehub.listen_color_sensor(PORT_C)

while True:
    sleep(1)
    print(mymovehub.last_color)
    espeak.synth(mymovehub.last_color)

