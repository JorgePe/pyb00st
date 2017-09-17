#!/usr/bin/env python3

from gattlib import GATTRequester
import sys
from .constants import *

#
# To Do:
# - exception handling
# - validate connection
#

class MoveHub:
    address = ""
    controller = ""
    req = GATTRequester

    def __init__(self, address, controller):
        self.address = address
        self.controller = controller
        self.req = GATTRequester(self.address, False, self.controller)
        self.connect()

    def connect(self):

        if self.req.is_connected():
            print("Already connected")
        else:
            print("Connecting...")
            sys.stdout.flush()
            self.req.connect(True)

    def is_connected(self):
        return self.req.is_connected()

    def getaddress(self):
        return self.address

    def getname(self):
        self.connect()
        devicename = self.req.read_by_handle(0x07)
        return devicename[0]

    def set_led_color(self, color):
        if color in LED_COLORS:
            self.connect()
            self.req.write_by_handle(HANDLE, SET_LED_COLOR[LED_COLORS.index(color)])

    def motor_timed(self, motor, time_ms, dutycycle_pct):
        if motor in MOTORS:
            if dutycycle_pct in range(-100, 101):
                command = MOTOR_TIMED_INI
                command += motor
                command += MOTOR_TIMED_MID
                t = time_ms.to_bytes(2, byteorder='little')
                command += t
                if dutycycle_pct < 0:
                    dutycycle_pct += 255
                command += bytes(bytes(chr(dutycycle_pct), 'latin-1'))
                command += MOTOR_TIMED_END

                self.req.write_by_handle(HANDLE, command)

    def motors_timed(self, motor, time_ms, dutycycle_pct_A, dutycycle_pct_B):
        if motor in MOTOR_PAIRS:
            if dutycycle_pct_A in range(-100, 101) and dutycycle_pct_B in range(-100, 101):
                command = MOTORS_TIMED_INI
                command += motor
                command += MOTORS_TIMED_MID
                t = time_ms.to_bytes(2, byteorder='little')
                command += t
                if dutycycle_pct_A < 0:
                    dutycycle_pct_A += 255
                command += bytes(bytes(chr(dutycycle_pct_A), 'latin-1'))
                if dutycycle_pct_B < 0:
                    dutycycle_pct_B += 255
                command += bytes(bytes(chr(dutycycle_pct_B), 'latin-1'))
                command += MOTORS_TIMED_END

                self.req.write_by_handle(HANDLE, command)
