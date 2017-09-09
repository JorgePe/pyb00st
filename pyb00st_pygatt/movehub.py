#!/usr/bin/env python3

import pygatt
#from constants import *
from pyb00st_pygatt.constants import *

#
# To Do:
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

    tilt_basic = True
    last_tilt = ''



    def __init__(self, address, controller):
        ''' Constructor for this class. '''
 
        self.address=address
        self.controller=controller

        self.adapter = pygatt.GATTToolBackend()
        self.adapter.start()
        self.connect()

    def connect(self):

        self.device = self.adapter.connect(self.address)

    def is_connected(self):
        ### Useless - needs thinking
        return True

    def getaddress(self):
        return self.address

    def getname(self):
        self.connect()
        devicename=self.device.char_read_handle(0x07)
        return devicename.decode("utf-8")

    def set_led_color(self, color):
        if color in LED_COLORS :
            self.device.write_handle(MOVE_HUB_HARDWARE_HANDLE, SET_LED_COLOR[LED_COLORS.index(color)] )

    def motor_timed(self, motor, time_ms, dutycycle_pct):
        if motor in MOTORS :
            if dutycycle_pct in range (-100,101) :
                command = MOTOR_TIMED_INI
                command += motor
                command += MOTOR_TIMED_MID
                t = time_ms.to_bytes(2, byteorder='little')
                command += t
                if dutycycle_pct < 0 :
                    dutycycle_pct += 255
                command += bytes( bytes( chr(dutycycle_pct), 'latin-1' ) )
                command += MOTOR_TIMED_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command )


    def motors_timed(self, motor, time_ms, dutycycle_pct_A, dutycycle_pct_B):
        if motor in MOTOR_PAIRS :
            if dutycycle_pct_A in range (-100,101) and dutycycle_pct_B in range (-100,101) :
                command = MOTORS_TIMED_INI
                command += motor
                command += MOTORS_TIMED_MID
                t = time_ms.to_bytes(2, byteorder='little')
                command += t
                if dutycycle_pct_A < 0 :
                    dutycycle_pct_A += 255
                command += bytes( bytes( chr(dutycycle_pct_A), 'latin-1' ) )
                if dutycycle_pct_B < 0 :
                    dutycycle_pct_B += 255
                command += bytes( bytes( chr(dutycycle_pct_B), 'latin-1' ) )
                command += MOTORS_TIMED_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command )


    def motor_angle(self, motor, angle, dutycycle_pct):
        if motor in MOTORS :
            if dutycycle_pct in range (-100,101) :
                command = MOTOR_ANGLE_INI
                command += motor
                command += MOTOR_ANGLE_MID
                ang = angle.to_bytes(4, byteorder='little')
                command += ang
                if dutycycle_pct < 0 :
                    dutycycle_pct += 255
                command += bytes( bytes( chr(dutycycle_pct), 'latin-1' ) )
                command += MOTOR_ANGLE_END

                self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, command )


#
# Sensors depend on Notifications
# we subscribe for notifications and activate the sensors we want
# then we are notified each time a sensor changes
#
# Considering using some kind of flag to indicate change of sensor values
#


    def parse_notifications(self, handle, value):
        # callback funtion
        if handle == MOVE_HUB_HARDWARE_HANDLE :

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
                value[2] == 0x45 :

                # Let's see what we have here

                if value[3] == PORT_A :
                    # It's an Encoded Motor

                    self.last_encoder_A = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                    if self.last_encoder_A > ENCODER_MID :
                        self.last_encoder_A = self.last_encoder_A - ENCODER_MAX


                elif value[3] == PORT_B :
                    # It's an Encoded Motor

                    self.last_encoder_B = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                    if self.last_encoder_B > ENCODER_MID :
                        self.last_encoder_B = self.last_encoder_B - ENCODER_MAX

                elif value[3] == PORT_C :

                    # Might be several things, need to know what we have on port C

                    if self.color_sensor_on_C == True:
                        if value[4] != 0xFF :
                            self.last_color_C = COLOR_SENSOR_COLORS[value[4]]
                        else:
                            self.last_color_C = ''

                    elif self.distance_sensor_on_C == True:
                        if value[4] == 0xFF :
                            self.last_distance_C = str(value[5])
                        else:
                            self.last_distance_C = ''

                    elif self.motor_encoder_on_C == True:

                        self.last_encoder_C = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                        if self.last_encoder_C > ENCODER_MID :
                            self.last_encoder_C = self.last_encoder_C - ENCODER_MAX


                elif value[3] == PORT_D :

                    # Might be several things, need to know what we have on port D

                    if self.color_sensor_on_D == True:
                        if value[4] != 0xFF :
                            self.last_color_D = COLOR_SENSOR_COLORS[value[4]]
                        else:
                            self.last_color_D = ''

                    elif self.distance_sensor_on_D == True:
                        if value[4] == 0xFF :
                            self.last_distance_D = str(value[5])
                        else:
                            self.last_distance_D = ''

                    elif self.motor_encoder_on_D == True:

                        self.last_encoder_D = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                        if self.last_encoder_D > ENCODER_MID :
                            self.last_encoder_D = self.last_encoder_D - ENCODER_MAX

                elif value[3] == PORT_AB :
                    # It's an Encoded Motor
                    # But message is different, will do it later
                    pass


            # Button
            # expected: 06 00 01 02 06 xx , xx = 00 / 01

            elif value[0] == 0x06 and \
                    value[1] == 0x00 and \
                    value[2] == 0x01 and \
                    value[3] == 0x02 and \
                    value[4] == 0x06 :

                    if value[5] == 1 :
                        self.last_button = BUTTON_PRESSED
                    elif value[5] == 0 :
                        self.last_button = BUTTON_RELEASED
                    else :
                        self.last_button = ''
            # Tilt Basic Mode
            # expected: 05 00 45 3a xx

            elif value[0] == 0x05 and \
                value[1] == 0x00 and \
                value[2] == 0x45 and \
                value[3] == 0x3a :

                    if value[4] in TILT_BASIC_VALUES :
                        self.last_tilt = value[4]
                    else:
                        self.last_tilt = ''
                        print('Tilt: Unknown value')    



    def subscribe_all(self):
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.parse_notifications)

# Color

    # Color Sensor can be at port C or D (probably also both)

    def listen_color_sensor(self, port):
        if port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_COLOR_SENSOR_ON_C)
            self.color_sensor_on_C = True
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_COLOR_SENSOR_ON_D)
            self.color_sensor_on_D = True


# Distance

    # Distance Sensor can be at port C or D (probably also both)

    def listen_distance_sensor(self, port):
        if port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_DIST_SENSOR_ON_C)
            self.distance_sensor_on_C = True
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_DIST_SENSOR_ON_D)
            self.distance_sensor_on_D = True


# Encoder

    def listen_encoder_sensor(self, port):
        if port == PORT_A :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_A)
        elif port == PORT_B :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_B)
        elif port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_C)
            self.motor_encoder_on_C = True
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_D)
            self.motor_encoder_on_D = True

# Button

    def listen_button(self):
        self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_BUTTON)


# Tilt

    def listen_tilt(self, tilt_basic):
        if tilt_basic == True:
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_TILT_BASIC)
        else:
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_TILT_FULL)
        self.tilt_basic = tilt_basic


