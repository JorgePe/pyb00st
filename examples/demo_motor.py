#!/usr/bin/env python3
'''Example script to show how to control motors'''

from time import sleep

from pyb00st import B00stConfig
from pyb00st.movehub import MoveHub
from pyb00st.constants import MOTOR_A, MOTOR_AB


def run():
    '''
    This function is required for pylint, without cfg and mymovehub are
    treated as constants
    '''
    cfg = B00stConfig()
    mymovehub = MoveHub(cfg.MY_MOVEHUB_ADD, 'BlueZ', cfg.MY_BTCTRLR_HCI)

    try:
        mymovehub.start()

        # turn motor A ON for 1000 ms at 100% duty cycle in both directions
        mymovehub.run_motor_for_time(MOTOR_A, 1000, 100)
        sleep(1)
        mymovehub.run_motor_for_time(MOTOR_A, 1000, -100)
        sleep(1)

        sleep(0.5)

        # rotate motor 90 degrees at 100% duty cycle in both directions
        mymovehub.run_motor_for_angle(MOTOR_A, 90, 100)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 90, -100)

        sleep(0.5)

        # turn pair AB ON for 1000 ms at 100% duty cycle in both direction
        mymovehub.run_motors_for_time(MOTOR_AB, 1000, 100, 100)
        sleep(1)
        mymovehub.run_motors_for_time(MOTOR_AB, 1000, 100, -100)
        sleep(1)
        mymovehub.run_motors_for_time(MOTOR_AB, 1000, -100, -100)
        sleep(1)
        mymovehub.run_motors_for_time(MOTOR_AB, 1000, -100, 100)
        sleep(1)

        sleep(0.5)

        # rotate pair AB 90 degrees at 100% duty cycle in both direction
        mymovehub.run_motors_for_angle(MOTOR_AB, 90, 100, 100)
        sleep(0.5)
        mymovehub.run_motors_for_angle(MOTOR_AB, 90, 100, -100)
        sleep(0.5)
        mymovehub.run_motors_for_angle(MOTOR_AB, 90, -100, -100)
        sleep(0.5)
        mymovehub.run_motors_for_angle(MOTOR_AB, 90, -100, 100)
        sleep(0.5)

    finally:
        mymovehub.stop()


if __name__ == '__main__':
    run()
