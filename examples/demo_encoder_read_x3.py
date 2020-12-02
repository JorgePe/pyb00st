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
    mymovehub.subscribe_all()
    mymovehub.listen_angle_sensor(PORT_A)
    mymovehub.listen_angle_sensor(PORT_B)
    mymovehub.listen_angle_sensor(PORT_D)

    while True:
        sleep(0.2)
        print('Motor A: {} Motor B: {} Motor D: {}'.
              format(mymovehub.last_angle_A, mymovehub.last_angle_B, mymovehub.last_angle_D))
finally:
    mymovehub.stop()
