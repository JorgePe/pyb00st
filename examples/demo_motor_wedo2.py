#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

import os

MY_MOVEHUB_ADD = os.environ.get('MYMOVEHUB')
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'BlueZ', MY_BTCTRLR_HCI)

try:
    mymovehub.start()

    # turn WeDo motor on port C ON for 500 ms at 100% duty cycle in both directions
    # then stop
    mymovehub.motor_wedo(PORT_C, 100)
    sleep(0.5)
    mymovehub.motor_wedo(PORT_C, -100)
    sleep(0.5)
    mymovehub.motor_wedo(PORT_C, 0)
finally:
    mymovehub.stop()
