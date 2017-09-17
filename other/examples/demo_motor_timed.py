#!/usr/bin/env python3

from time import sleep

from ..pyboost import constants
from ..pyboost import movehub

MY_MOVEHUB_ADD = "00:16:53:A4:CD:7E"
MY_BTCTRLR_HCI = "hci0"

mymovehub = movehub.MoveHub(MY_MOVEHUB_ADD, MY_BTCTRLR_HCI)

period_ms = 400
dutycycle_pct = 100

mymovehub.motors_timed(constants.MOTOR_AB, period_ms, -dutycycle_pct, dutycycle_pct)
sleep(period_ms/1000)

period_ms = 200

mymovehub.motor_timed(constants.MOTOR_A, period_ms, -dutycycle_pct)
sleep(period_ms/1000)

mymovehub.motor_timed(constants.MOTOR_B, period_ms, dutycycle_pct)
sleep(period_ms/1000)
