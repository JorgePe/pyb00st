#!/usr/bin/env python3

from pyb00st_pygatt.movehub import MoveHub
from pyb00st_pygatt.constants import *

from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)

# turn motor A ON for 1000 ms at 100% duty cycle in both directions
mymovehub.motor_timed(MOTOR_A, 1000, 100)
sleep(1)
mymovehub.motor_timed(MOTOR_A, 1000, -100)
sleep(1)

sleep(0.5)

# rotate motor 90 degrees at 100% duty cycle in both directions
mymovehub.motor_angle(MOTOR_A, 90, 100)
sleep(0.5)
mymovehub.motor_angle(MOTOR_A, 90, -100)

sleep(0.5)

# turn pair AB ON for 1000 ms at 100% duty cycle in both direction
mymovehub.motors_timed(MOTOR_AB, 1000, 100, 100)
sleep(1)
mymovehub.motors_timed(MOTOR_AB, 1000, 100, -100)
sleep(1)
mymovehub.motors_timed(MOTOR_AB, 1000, -100, -100)
sleep(1)
mymovehub.motors_timed(MOTOR_AB, 1000, -100, 100)
sleep(1)

sleep(0.5)

# rotate pair AB 90 degrees at 100% duty cycle in both direction
mymovehub.motors_angle(MOTOR_AB, 90, 100, 100)
sleep(0.5)
mymovehub.motors_angle(MOTOR_AB, 90, 100, -100)
sleep(0.5)
mymovehub.motors_angle(MOTOR_AB, 90, -100, -100)
sleep(0.5)
mymovehub.motors_angle(MOTOR_AB, 90, -100, 100)
sleep(0.5)
