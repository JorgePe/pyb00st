#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'

# not used - need to find how where on pygatt we can choose the hci controller
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_button()
mymovehub.listen_button()

while True:
    sleep(0.2)
    if mymovehub.last_button == BUTTON_PRESSED :
        print('PRESSED')
    elif mymovehub.last_button == BUTTON_RELEASED :
        print('RELEASED')
    else:
        print('')
