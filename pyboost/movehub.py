#!/usr/bin/env python3

from gattlib import GATTRequester
import sys

from constants import *

#
# To Do:
# - exception handling
#


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
