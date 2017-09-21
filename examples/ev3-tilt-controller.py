#!/usr/bin/env python3

#
# This example runs only on ev3dev
#

from pyb00st.movehub import MoveHub
from pyb00st.constants import *
import ev3dev.ev3 as ev3

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci1'

m1 = ev3.LargeMotor('outA')
m2 = ev3.LargeMotor('outB')

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'BlueZ', MY_BTCTRLR_HCI)
mymovehub.subscribe_all()
mymovehub.listen_hubtilt(MODE_HUBTILT_BASIC)

while True:
    tilt = mymovehub.last_hubtilt
    if tilt in TILT_BASIC_VALUES:
        if tilt == TILT_HORIZ:
            pass
        elif tilt == TILT_UP:
            m1.run_timed(time_sp=125, speed_sp=-720)
            m2.run_timed(time_sp=125, speed_sp=-720)
            sleep(0.125)
        elif tilt == TILT_DOWN:
            m1.run_timed(time_sp=125, speed_sp=720)
            m2.run_timed(time_sp=125, speed_sp=720)
            sleep(0.125)
        elif tilt == TILT_RIGHT:
            m1.run_timed(time_sp=125, speed_sp=360)
            m2.run_timed(time_sp=125, speed_sp=-360)
            sleep(0.1)
        elif tilt == TILT_LEFT:
            m1.run_timed(time_sp=125, speed_sp=-360)
            m2.run_timed(time_sp=125, speed_sp=360)
            sleep(0.1)
        elif tilt == TILT_INVERT:
            pass


