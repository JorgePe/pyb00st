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
    mymovehub.listen_colordist_sensor(PORT_C)

    while True:
        sleep(0.2)
        print('Color: {} Distance: {}'.format(mymovehub.last_color_C, mymovehub.last_distance_C))

finally:
    mymovehub.stop()
