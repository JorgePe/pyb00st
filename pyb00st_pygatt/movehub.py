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
    controller = ""
    last_color = ''
    last_distance = ''
    last_encoder_port = ''
    last_encoder_angle = ''
    last_button = ''

    color_sensor_port = ''   # to know where the sensor is inserted so we can
                               # understand notifications

    distance_sensor_port = ''   # to know where the sensor is inserted so we can
                                  # understand notifications

    def __init__(self, address, controller):
        ''' Constructor for this class. '''
 
        self.address=address
        self.controller=controller

#        self.req = GATTRequester(self.address,False,self.controller)
#        self.connect()

        self.adapter = pygatt.GATTToolBackend()
        self.adapter.start()
        self.connect()

    def connect(self):

        self.device = self.adapter.connect(self.address)

    def is_connected(self):
        ### Needs thinking
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

#                print("Final Command:", command)
#                i=0
#                for x in command:
#                    print( i, x )
#                    i+=1

                self.device.write_handle(MOVE_HUB_HARDWARE_HANDLE, command )


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

#                print("Final Command:", command)
#                i=0
#                for x in command:
#                    print( i, x )
#                    i+=1

                self.device.write_handle(MOVE_HUB_HARDWARE_HANDLE, command )



#
# Caution!
# Sensors are not finished yet
# notifications are not proper checked for each sensor
# so be sure to initialize just one sensor
#


# Color

    def listen_color_sensor(self, port):
        if port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_COLOR_SENSOR_ON_C)
            self.color_sensor_port = port
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_COLOR_SENSOR_ON_D)
            self.color_sensor_port = port

    def read_color_sensor(self, handle, value):
        # callback funtion
        if handle == MOVE_HUB_HARDWARE_HANDLE :

            # expected: 08 00 45 pp xx aa bb cc
            # pp = port
            # xx = FF or color
            # aa, bb, cc = unknown

            # we assume only 1 color sensor is possible

            if value[0] == 0x08 and \
                value[1] == 0x00 and \
                value[2] == 0x45 and \
                value[3] == self.color_sensor_port :

                if value[4] != 0xFF :
                    self.last_color = COLOR_SENSOR_COLORS[value[4]]
                else:
                    self.last_color = ''

    def subscribe_color(self):
        # we assume only 1 color sensor is possible
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.read_color_sensor)


# Distance

    def listen_distance_sensor(self, port):
        if port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_DIST_SENSOR_ON_C)
            self.distance_sensor_port = port
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_DIST_SENSOR_ON_D)
            self.distance_sensor_port = port

    def read_distance_sensor(self, handle, value):
        # callback funtion
        if handle == MOVE_HUB_HARDWARE_HANDLE :
           # expected: 08 00 45 pp aa xx bb cc 
            # pp = port
            # xx = distance
            # aa, bb, cc = unknown

            # we assume only 1 distance sensor is possible

            if value[0] == 0x08 and \
                value[1] == 0x00 and \
                value[2] == 0x45 and \
                value[3] == self.distance_sensor_port :

                if value[4] == 0xFF :
                    self.last_distance = str(value[5])
                else:
                    self.last_distance = ''

    def subscribe_distance(self):
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.read_distance_sensor)

# Encoder #

    def listen_encoder_sensor(self, port):
        if port == PORT_A :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_A)
        elif port == PORT_B :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_B)
        elif port == PORT_C :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_C)
        elif port == PORT_D :
            self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_ENCODER_ON_D)

    def read_encoder_sensor(self, handle, value):
        # callback funtion
        # probably will have to make a callback function for every encoder

        if handle == MOVE_HUB_HARDWARE_HANDLE :

            # expected: 08 00 45 pp xx xx xx xx
            # pp = port
            # xx xx xx xx = angle

            if value[0] == 0x08 and \
                value[1] == 0x00 and \
                value[2] == 0x45 :

                self.last_encoder_port = value[3]

                self.last_encoder_angle = value[4] + value[5]*256 + value[6]*65536 + value[7]*16777216
                if self.last_encoder_angle > ENCODER_MID :
                    self.last_encoder_angle = self.last_encoder_angle - ENCODER_MAX

    def subscribe_encoder(self):
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.read_encoder_sensor)

# Button

    def listen_button(self):
        self.device.char_write_handle(MOVE_HUB_HARDWARE_HANDLE, LISTEN_BUTTON)

    def read_button(self, handle, value):
        # callback funtion

        if handle == MOVE_HUB_HARDWARE_HANDLE :
            # expected: 06 00 01 02 06 xx , xx = 00 / 01

            if value[0] == 0x06 and \
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

    def subscribe_button(self):
        self.device.subscribe(MOVE_HUB_HARDWARE_UUID, self.read_button)



