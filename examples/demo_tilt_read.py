#!/usr/bin/env python3

from pyb00st import B00stConfig
from pyb00st.movehub import MoveHub
from pyb00st.constants import MODE_HUBTILT_BASIC, TILT_BASIC_VALUES, TILT_BASIC_TEXT

from time import sleep

CFG = B00stConfig()

mymovehub = MoveHub(CFG.MY_MOVEHUB_ADD, 'Auto', CFG.MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    print(mymovehub.backend)
    mymovehub.subscribe_all()
    mymovehub.listen_hubtilt(MODE_HUBTILT_BASIC)

    while True:
        sleep(0.2)
        if mymovehub.last_hubtilt in TILT_BASIC_VALUES:
            print(TILT_BASIC_TEXT[mymovehub.last_hubtilt])
except KeyboardInterrupt:
    print("\nCTRL-C pressed! Exiting ...")
finally:
    mymovehub.stop()
