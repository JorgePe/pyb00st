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
    mymovehub.listen_button()

    while True:
        sleep(0.2)
        if mymovehub.last_button == BUTTON_PRESSED:
            print('PRESSED')
        elif mymovehub.last_button == BUTTON_RELEASED:
            print('RELEASED')
        else:
            print('')
except KeyboardInterrupt:
    print("\nCTRL-C pressed! Exiting ...")
finally:
    mymovehub.stop()
