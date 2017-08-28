#!/usr/bin/env python3

from gattlib import GATTRequester
import sys

#
# To Do:
# - exception handling
#

class movehub:
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

    def getAddress(self):
        return self.address

    def getName(self):
        self.connect()
        devicename=self.req.read_by_handle(0x07)
        return devicename[0]

