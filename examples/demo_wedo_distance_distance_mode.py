#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.subscribe_all()
    mymovehub.listen_wedo_distance(PORT_D, MODE_WEDODIST_DISTANCE)

    while True:
        sleep(0.2)
        print(mymovehub.last_wedo_distance_D)

finally:
    mymovehub.stop()
