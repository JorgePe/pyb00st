#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

import os
#
#  Line Follower
#  - wheels on motor A and B
#  - ColorDist sensor on port C
#  Demo video: https://youtu.be/2QysaaYmy9Q
#

MY_MOVEHUB_ADD = os.environ.get('MYMOVEHUB')
MY_BTCTRLR_HCI = 'hci0'

delay = 0.0 # delay at the end of each cycle

def front():
    mymovehub.run_motors_for_time(MOTOR_AB, 100, 20, 20)
    sleep(0.1)

def left():
    mymovehub.run_motors_for_time(MOTOR_AB, 100, -100, 100)
    sleep(0.1)

def right():
    mymovehub.run_motors_for_time(MOTOR_AB, 200, 100, -100)
    sleep(0.2)

def back():
    mymovehub.run_motors_for_time(MOTOR_AB, 100, -20, -20)
    sleep(0.1)

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'Auto', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.subscribe_all()
    mymovehub.listen_colordist_sensor(PORT_C)

    while True:
        color = mymovehub.last_color_C
        print(color)
        if color in ['BLACK','BLUE']:
            back()
            right()
        elif color in ['WHITE', 'YELLOW', 'RED']:
            front()
            left()
        else:
            pass

finally:
    mymovehub.stop()
