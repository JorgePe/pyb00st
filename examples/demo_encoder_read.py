#!/usr/bin/env python3

from pyb00st import B00stConfig
from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

CFG = B00stConfig()

mymovehub = MoveHub(CFG.MY_MOVEHUB_ADD, 'BlueZ', CFG.MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.subscribe_all()
    mymovehub.listen_angle_sensor(PORT_C)

    while True:
        sleep(0.2)
        print(mymovehub.last_angle_C)
except KeyboardInterrupt:
    print("\nCTRL-C pressed! Exiting ...")
finally:
    mymovehub.stop()
