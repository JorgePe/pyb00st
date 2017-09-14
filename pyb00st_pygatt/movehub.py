#!/usr/bin/env python3

import pygatt
from pyb00st_pygatt.constants import *

#
# To Do:
# - create a list of devices instead of using so many variables
# - exception handling
# - validate connection
#


class MoveHub:
    address = ""

    color_sensor_on_C = False
    color_sensor_on_D = False

    distance_sensor_on_C = False
    distance_sensor_on_D = False

    motor_encoder_on_C = False
    motor_encoder_on_D = False

    tilt_basic = True

    last_color_C = ''
    last_color_D = ''

    last_distance_C = ''
    last_distance_D = ''

    last_encoder_A = ''
    last_encoder_B = ''
    last_encoder_C = ''
    last_encoder_D = ''
    last_encoder_AB = ''

    last_button = ''

    last_tilt = ''

    last_wedo_tilt_C_roll = ''
    last_wedo_tilt_C_pitch = ''
    last_wedo_tilt_D_roll = ''
    last_wedo_tilt_D_pitch = ''
    last_wedo_tilt_C_tilt = ''
    last_wedo_tilt_D_tilt = ''
    last_wedo_tilt_C_crash = ''
    last_wedo_tilt_D_crash = ''

    last_wedo_distance_C = ''
    last_wedo_distance_D = ''

    wedo_tilt_mode = ''
    wedo_tilt_on_C = False
    wedo_tilt_on_D = False

    wedo_distance_mode = ''
    wedo_distance_on_C = False
    wedo_distance_on_D = False

    def __init__(self, address, controller): 
        self.address = address
        self.controller = controller

#
# from pygatt source code, GATTToolBackend acepts:
# hci_device='hci0', gatttool_logfile=None,cli_options=None
#
        self.adapter = pygatt.GATTToolBackend(hci_device=controller)
        self.adapter.start()

# connect - missing disconnect method
        self.device = self.adapter.connect(self.address)

    def is_connected(self):
        # Useless - needs thinking
        return True

    def getaddress(self):
        return self.address

    def getname(self):
        devicename = self.device.char_read_handle(0x07)
        return devicename.decode("utf-8")

#
#
# set_led_color()
#  accepts one of the 10 colors (plus Off) defined in constants.py
#
#
    def set_led_color(self, color):
        if color in LED_COLORS:
            self.device.write_handle(MOVE_HUB_HARDWARE_HANDLE, SET_LED_COLOR[LED_COLORS.index(color)])

#
#
# motor_timed()
# motors_timed()
#  accepts a motor (defined in constants.py), a time in milliseconds and a dutycycle in percentage
#  to change direction use negative dutycycle
#  should find a way to merge the 2 methods, later on
#
#
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

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

    def motors_timed(self, motor, time_ms, dutycycle_pct_a, dutycycle_pct_b):
        if motor in MOTOR_PAIRS:
            if dutycycle_pct_a in range(-100, 101) and dutycycle_pct_b in range(-100, 101):
                command = MOTORS_TIMED_INI
                command += motor
                command += MOTORS_TIMED_MID
                t = time_ms.to_bytes(2, byteorder='little')
                command += t
                if dutycycle_pct_a < 0:
                    dutycycle_pct_a += 255
                command += bytes(bytes(chr(dutycycle_pct_a), 'latin-1'))
                if dutycycle_pct_b < 0:
                    dutycycle_pct_b += 255
                command += bytes(bytes(chr(dutycycle_pct_b), 'latin-1'))
                command += MOTORS_TIMED_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

#
#
# motor_angle()
# motors_angle()
#  accepts a motor (defined in constants.py), an angle in degrees and a dutycycle in percentage
#  to change direction use negative dutycycle
#  should find a way to merge the 2 methods, later on
#
#
    def motor_angle(self, motor, angle, dutycycle_pct):
        if motor in MOTORS:
            if dutycycle_pct in range(-100, 101):
                command = MOTOR_ANGLE_INI
                command += motor
                command += MOTOR_ANGLE_MID
                ang = angle.to_bytes(4, byteorder='little')
                command += ang
                if dutycycle_pct < 0:
                    dutycycle_pct += 255
                command += bytes(bytes(chr(dutycycle_pct), 'latin-1'))
                command += MOTOR_ANGLE_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

    def motors_angle(self, motor, angle, dutycycle_pct_a, dutycycle_pct_b):
        if motor in MOTORS:
            if dutycycle_pct_a in range(-100, 101) and dutycycle_pct_b in range(-100, 101):
                command = MOTORS_ANGLE_INI
                command += motor
                command += MOTORS_ANGLE_MID
                ang = angle.to_bytes(4, byteorder='little')
                command += ang
                if dutycycle_pct_a < 0:
                    dutycycle_pct_a += 255
                command += bytes(bytes(chr(dutycycle_pct_a), 'latin-1'))
                if dutycycle_pct_b < 0:
                    dutycycle_pct_b += 255
                command += bytes(bytes(chr(dutycycle_pct_b), 'latin-1'))
                command += MOTORS_ANGLE_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

#
#
# motor_wedo()
# - external device, can be at port C or D or both
#  accepts a port and a dutycycle in percentage
#  to change direction use negative dutycycle
#  to stop use zero dutycycle
#
#

    def motor_wedo(self, port, dutycycle_pct):
        if port == PORT_C or port == PORT_D:
            if dutycycle_pct in range(-100, 101):
                command = MOTOR_WEDO_INI
                command += bytes([port])
                command += MOTOR_WEDO_MID
                if dutycycle_pct < 0:
                    dutycycle_pct += 255
                command += bytes(bytes(chr(dutycycle_pct), 'latin-1'))

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

#
#
# Sensors depend on Notifications
# we subscribe for notifications and activate the sensors we want to be notified
# notifications are sent each time an active sensor changes
#
# currently, an internal variable holds last sensor value
# so we have to poll the variable
#
#
    def parse_notifications(self, handle, value):
        # callback funtion
        if handle == MOVE_HUB_HARDWARE_HANDLE:

            # Color Sensor
            # expected: 08 00 45 pp xx aa bb cc
            # pp = port
            # xx = FF or color
            # aa, bb, cc = unknown

            # Distance Sensor
            # expected: 08 00 45 pp aa xx bb cc 
            # pp = port
            # xx = distance
            # aa, bb, cc = unknown

            # Encoder
            # expected: 08 00 45 pp xx xx xx xx
            # pp = port
            # xx xx xx xx = angle

            if value[0] == 0x08 and \
                    value[1] == 0x00 and \
                    value[2] == 0x45:

                # Let's see what we have here

                if value[3] == PORT_A:
                    # It's an Encoded Motor

                    self.last_encoder_A = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                    if self.last_encoder_A > ENCODER_MID:
                        self.last_encoder_A = self.last_encoder_A - ENCODER_MAX

                elif value[3] == PORT_B:
                    # It's an Encoded Motor

                    self.last_encoder_B = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                    if self.last_encoder_B > ENCODER_MID:
                        self.last_encoder_B = self.last_encoder_B - ENCODER_MAX

                elif value[3] == PORT_C:

                    # Might be several things, need to know what we have on port C

                    if self.color_sensor_on_C:
                        if value[4] != 0xFF:
                            self.last_color_C = COLOR_SENSOR_COLORS[value[4]]
                        else:
                            self.last_color_C = ''

                    elif self.distance_sensor_on_C:
                        if value[4] == 0xFF:
                            self.last_distance_C = str(value[5])
                        else:
                            self.last_distance_C = ''

                    elif self.motor_encoder_on_C:

                        self.last_encoder_C = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                        if self.last_encoder_C > ENCODER_MID:
                            self.last_encoder_C = self.last_encoder_C - ENCODER_MAX

                elif value[3] == PORT_D:

                    # Might be several things, need to know what we have on port D

                    if self.color_sensor_on_D:
                        if value[4] != 0xFF:
                            self.last_color_D = COLOR_SENSOR_COLORS[value[4]]
                        else:
                            self.last_color_D = ''

                    elif self.distance_sensor_on_D:
                        if value[4] == 0xFF:
                            self.last_distance_D = str(value[5])
                        else:
                            self.last_distance_D = ''

                    elif self.motor_encoder_on_D:

                        self.last_encoder_D = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                        if self.last_encoder_D > ENCODER_MID:
                            self.last_encoder_D = self.last_encoder_D - ENCODER_MAX

                elif value[3] == MOTOR_AB:
                    # It's an Encoded Motor
                    # But message is different, will do it later
                    pass

            # Button
            # expected: 06 00 01 02 06 xx , xx = 00 / 01

            elif value[0] == 0x06 and \
                    value[1] == 0x00 and \
                    value[2] == 0x01 and \
                    value[3] == 0x02 and \
                    value[4] == 0x06:

                if value[5] == 1:
                    self.last_button = BUTTON_PRESSED
                elif value[5] == 0:
                    self.last_button = BUTTON_RELEASED
                else:
                    self.last_button = ''

            # Tilt Basic Mode
            # expected: 05 00 45 3a xx

            elif value[0] == 0x05 and \
                    value[1] == 0x00 and \
                    value[2] == 0x45 and \
                    value[3] == 0x3a:

                if value[4] in TILT_BASIC_VALUES:
                    self.last_tilt = value[4]
                else:
                    self.last_tilt = ''
                    print('Tilt: Unknown value')    

            # WeDo Tilt, Angle Mode
            # expected: 06 00 45 port xx yy, xx = roll, yy = pitch

            elif value[0] == 0x06 and \
                    value[1] == 0x00 and \
                    value[2] == 0x45:

                if value[3] == PORT_C:
                    self. last_wedo_tilt_C_roll = int(value[4])
                    self.last_wedo_tilt_C_pitch = int(value[5])

                elif value[3] == PORT_D:
                    self.last_wedo_tilt_D_roll = int(value[4])
                    self.last_wedo_tilt_D_pitch = int(value[5])

            # WeDo Tilt, Tilt Mode
            # expected: 05 00 45 port xx, xx = tilt values
            # WeDo Distance, Distance Mode
            # expected: 05 00 45 port xx, xx = distance 00..0A

            elif value[0] == 0x05 and \
                    value[1] == 0x00 and \
                    value[2] == 0x45:

                if value[3] == PORT_C:
                    if self.wedo_tilt_on_C:
                        self.last_wedo_tilt_C_tilt = int(value[4])
                    elif self.wedo_distance_on_C:
                        self.last_wedo_distance_C = int(value[4])

                elif value[3] == PORT_D:
                    if self.wedo_tilt_on_D:
                        self.last_wedo_tilt_D_tilt = int(value[4])
                    elif self.wedo_distance_on_D:
                        self.last_wedo_distance_D = int(value[4])

            # WeDo Tilt, Crash Mode
            # expected: 07 00 45 port xx yy zz, these 3 bytes are incremented up to 0x64

            elif value[0] == 0x07 and \
                    value[1] == 0x00 and \
                    value[2] == 0x45:

                if value[3] == PORT_C:
                    self.last_wedo_tilt_C_crash = [value[4], value[5], value[6]]
                elif value[3] == PORT_D:
                    self.last_wedo_tilt_D_crash = [value[4], value[5], value[6]]

    def subscribe_all(self):
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.parse_notifications)

#
#
# Methods that activate sensors
# (no method for deactivate yet)
#
#

#
# Color Sensor
# - external device, can be at port C or D (probably also at both)
#
    def listen_colordist_sensor(self, port):
        if port in [PORT_C, PORT_D]:
            command = LISTEN_INI
            command += bytes([port])
            command += MODE_COLORDIST_SENSOR
            command += LISTEN_END

            if port == PORT_C:
                self.color_sensor_on_C = True
            else:
                self.color_sensor_on_D = True

            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

#
# Encoder Sensor
# - there are 2 intenal encoders at ports A and B
# - there is also an external Interactive Motor, can be at port C or D (probably also at both)
# - missing reading of port group AB
#
    def listen_encoder_sensor(self, port):
        if port in [PORT_A, PORT_B, PORT_C, PORT_D]:
            command = LISTEN_INI
            command += bytes([port])
            command += MODE_ENCODER
            command += LISTEN_END

            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)
#
# Button Sensor
# - internal device, reacts to PRESS and DEPRESS actions
#

    def listen_button(self):
        self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_BUTTON)

#
# Tilt Sensor
# - internal device, reacts to pitch and roll (but not yaw, at least with current firmware)
# - at least two modes: basic and full
# - basic mode returns only to 6 extreme 90º positions defined at constants.py 
# - full mode (still missing) returns all positions, 1º resolution
#
    def listen_tilt(self, tilt_basic):
        command = LISTEN_INI
        command += bytes([PORT_TILT])
        if tilt_basic:
            command += MODE_TILT_BASIC
        else:
            command += MODE_TILT_FULL
        command += LISTEN_END

        self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

#
# WeDo Tilt Sensor
# - external device, can be at port C or D (probably also on both)
# - modes: angle, tilt, crash
#

    def listen_wedo_tilt(self, port, mode=MODE_WEDOTILT_ANGLE):
        if port in [PORT_C, PORT_D] and \
                mode in [MODE_WEDOTILT_ANGLE, MODE_WEDOTILT_TILT, MODE_WEDOTILT_CRASH]:

            self.wedo_tilt_mode = mode
            command = LISTEN_INI
            command += bytes([port])
            command += mode
            command += LISTEN_END

            if port == PORT_C:
                self.wedo_tilt_on_C = True
                self.wedo_distance_on_C = False
            elif port == PORT_D:
                self.wedo_tilt_on_D = True
                self.wedo_distance_on_D = False

            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)

        #
# WeDo Distance Sensor
# - external device, can be at port C or D (probably also on both)
# - modes: distance, trigger? , luminosity?
#

    def listen_wedo_distance(self, port, mode=MODE_WEDODIST_DISTANCE):
        if port in [PORT_C, PORT_D] and \
                mode in [MODE_WEDODIST_DISTANCE]:

            self.wedo_distance_mode = mode
            command = LISTEN_INI
            command += bytes([port])
            command += mode
            command += LISTEN_END

            if port == PORT_C:
                self.wedo_distance_on_C = True
                self.wedo_tilt_on_C = False
            elif port == PORT_D:
                self.wedo_distance_on_D = True
                self.wedo_tilt_on_D = False

            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command)
