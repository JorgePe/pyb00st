#!/usr/bin/env python3

from pyb00st import MoveHub
from pyb00st.constants import *
from time import sleep

MY_MOVEHUB_ADD = "00:16:53:A4:CD:7E"
MY_BTCTRLR_HCI = "hci0"

mymovehub = MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)

period_ms = 400
dutycycle_pct = 100

mymovehub.motors_timed(MOTOR_AB, period_ms, -dutycycle_pct, dutycycle_pct)
sleep(period_ms/1000)

period_ms = 200

mymovehub.motor_timed(MOTOR_A, period_ms, -dutycycle_pct)
sleep(period_ms/1000)

mymovehub.motor_timed(MOTOR_B, period_ms, dutycycle_pct)
sleep(period_ms/1000)
