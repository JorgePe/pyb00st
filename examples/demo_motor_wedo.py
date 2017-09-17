#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)

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
