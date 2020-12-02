#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

import os

MY_MOVEHUB_ADD = os.environ.get('MYMOVEHUB')
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'BlueZ', MY_BTCTRLR_HCI)
#mymovehub = MoveHub(MY_MOVEHUB_ADD, 'BlueGiga', '')
#mymovehub = MoveHub(MY_MOVEHUB_ADD, 'Auto', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    print(mymovehub.backend)
    mymovehub.subscribe_all()
    mymovehub.listen_hubtilt(MODE_HUBTILT_BASIC)

    while True:
        sleep(0.2)
        if mymovehub.last_hubtilt in TILT_BASIC_VALUES:
            print(TILT_BASIC_TEXT[mymovehub.last_hubtilt])
finally:
    mymovehub.stop()

