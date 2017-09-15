#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_all()
mymovehub.listen_wedo_tilt(PORT_C, WEDO_TILT_MODE_TILT)

while True:
    sleep(0.2)
    tilt = mymovehub.last_wedo_tilt_C_tilt
    if tilt == WEDO_TILT_HORIZ:
        print('HORIZ')
    elif tilt == WEDO_TILT_LEFT:
        print('LEFT')
    elif tilt == WEDO_TILT_RIGHT:
        print('RIGHT')
    elif tilt == WEDO_TILT_UP:
        print('UP')
    elif tilt == WEDO_TILT_DOWN:
        print('DOWN')


