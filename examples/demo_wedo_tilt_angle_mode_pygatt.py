#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_all()
mymovehub.listen_wedo_tilt(PORT_C, WEDO_TILT_MODE_ANGLE)

while True:
    sleep(0.2)
    print(mymovehub.last_wedo_tilt_C_roll, mymovehub.last_wedo_tilt_C_pitch)


