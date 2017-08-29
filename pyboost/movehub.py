#!/usr/bin/env python3

from gattlib import GATTRequester
import sys

#
# To Do:
# - exception handling
#

#
# Constants
#

HANDLE = 0x0E

# Commands:

# Commands for setting RGB LED color
SET_LED_OFF = b'\x08\x00\x81\x32\x11\x51\x00\x00'
SET_LED_PINK = b'\x08\x00\x81\x32\x11\x51\x00\x01'
SET_LED_PURPLE = b'\x08\x00\x81\x32\x11\x51\x00\x02'
SET_LED_BLUE = b'\x08\x00\x81\x32\x11\x51\x00\x03'
SET_LED_LIGHTBLUE = b'\x08\x00\x81\x32\x11\x51\x00\x04'
SET_LED_CYAN = b'\x08\x00\x81\x32\x11\x51\x00\x05'
SET_LED_GREEN = b'\x08\x00\x81\x32\x11\x51\x00\x06'
SET_LED_YELLOW = b'\x08\x00\x81\x32\x11\x51\x00\x07'
SET_LED_ORANGE = b'\x08\x00\x81\x32\x11\x51\x00\x08'
SET_LED_RED = b'\x08\x00\x81\x32\x11\x51\x00\x09'
SET_LED_WHITE = b'\x08\x00\x81\x32\x11\x51\x00\x0A'

SET_LED_COLOR = [SET_LED_OFF,
        SET_LED_PINK,
        SET_LED_PURPLE,
        SET_LED_BLUE,
        SET_LED_LIGHTBLUE,
        SET_LED_CYAN,
        SET_LED_GREEN,
        SET_LED_YELLOW,
        SET_LED_ORANGE,
        SET_LED_RED,
        SET_LED_WHITE]

# Colors:
LED_COLORS = ['OFF','PINK','PURPLE','BLUE','LIGHTBLUE','CYAN','GREEN','YELLOW','ORANGE','RED','WHITE']


class MoveHub:
    address = ""
    controller = ""
    req = GATTRequester

    def __init__(self, address, controller):
        ''' Constructor for this class. '''
 
        self.address=address
        self.controller=controller
        self.req = GATTRequester(self.address,False,self.controller)
        self.connect()


#
# Connect:
# - need to check if connection is OK or not
#
    def connect(self):

        if self.req.is_connected() == True :
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
        devicename=self.req.read_by_handle(0x07)
        return devicename[0]

    def set_led_color(self, color):
        if color in LED_COLORS :
            self.connect()
            self.req.write_by_handle(HANDLE, SET_LED_COLOR[LED_COLORS.index(color)] )
