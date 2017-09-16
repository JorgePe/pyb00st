#!/usr/bin/env python3

#
# This example needs the color sensor at PORT C
# and same sort of car with wheels on PORT A and B
# video: https://youtu.be/8XWXnisMeAY
#

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)
mymovehub.subscribe_all()
mymovehub.listen_color_sensor(PORT_C)

while True:
    color = mymovehub.last_color_C
    if color in COLOR_SENSOR_COLORS:
        if color == 'BLUE':
            mymovehub.run_motors_for_time(MOTOR_A, 500, -100, -100)
            sleep(0.5)
        elif color == 'WHITE':
            mymovehub.run_motor_for_time(MOTOR_A, 500, -100)
            sleep(0.5)
        elif color == 'YELLOW':
            mymovehub.run_motor_for_time(MOTOR_B, 500, -100)
            sleep(0.5)
        elif color == 'RED':
            mymovehub.run_motors_for_time(MOTOR_AB, 500, 100, 100)
            sleep(0.5)

