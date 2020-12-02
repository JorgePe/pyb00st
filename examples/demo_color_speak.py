#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from espeak import espeak  # apt install python3-espeak
from time import sleep

import os

MY_MOVEHUB_ADD = os.environ.get('MYMOVEHUB')
MY_BTCTRLR_HCI = 'hci0'

espeak.set_voice = 'en'

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'BlueZ', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.subscribe_all()
    mymovehub.listen_colordist_sensor(PORT_C)

    while True:
        sleep(1)
        print(mymovehub.last_color_C)
        espeak.synth(mymovehub.last_color_C)

finally:
    mymovehub.stop()
