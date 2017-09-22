#!/usr/bin/env python3

# This demo only works in linux
# It uses a Bluetooth Gamepad that is regognized as an HID device
# BLUETOOTH HID v1.1b Keyboard [Bluetooth Gamepad]
#
# before start make sure gamepad is paired
# evdev library needs root/sudo or user member of plugdev / input
#
# ls -l /dev/input/
# crw-rw---- 1 root input 13, 64 set 21 09:25 event0
#
# On Ubuntu, adding my user to group input
# didn't work so I had to
#
# sudo chmod 777 /dev/input/event20
#
# and repeat if the gamepad enters sleep mode
#
# can check the device with python3 -m evdev.evtest
# 20  /dev/input/event20   Bluetooth Gamepad                   34:f3:9a:88:60:7a
#
# This also only works with BlueGiga adapter.
# I think BlueZ backend doesn't work when HCI controller already
# paired with the gamepad
#

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

from time import sleep
import evdev
import threading

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

MY_GAMEPAD_NAME = 'Bluetooth Gamepad'

#
# MotorThread is always running
# motors are controlled by changing right/left duty cycles
#

class MotorThread(threading.Thread):

    right_dc = 0
    left_dc = 0

    def __init__(self):
        self.running = True
        threading.Thread.__init__(self)
        print("Ready")

    def run(self):
        while self.running:
            if self.left_dc != 0:
                mymovehub.run_motor_for_time(MOTOR_B, 200, self.left_dc)
            if self.right_dc != 0:
                mymovehub.run_motor_for_time(MOTOR_A, 200, self.right_dc)
            if self.left_dc != 0 or self.right_dc != 0:
                sleep(0.2)

#
# Find Bluetooth Gamepad
#

gamepad_found = False
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if device.name == MY_GAMEPAD_NAME:
        my_gamepad = evdev.InputDevice(device.fn)
        gamepad_found = True

if gamepad_found == False:
    print('\'{}\' not found'.format(MY_GAMEPAD_NAME))
    exit()
else:
    print('Gamepad found')

#
# Connect to BOOST Move Hub
#

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'Auto', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    motor_thread = MotorThread()
    motor_thread.setDaemon(True)
    motor_thread.start()

    for event in my_gamepad.read_loop():
        #print(event)
        if event.type == 3:
            # joystick or pad event

            # Y in [0..255] where 0 = max front, 128 = middle, 255 = max back
            if event.code == 0:
                # left.joystick,  X
                pass

            if event.code == 1:
                # left.joystick,  Y
                MotorThread.left_dc = int((event.value - 128)/1.28)

            if event.code == 5:
                # right joystick, Y
                MotorThread.right_dc = int((event.value - 128)/1.28)

            if event.code == 2:
                # right joystick, X
                pass

finally:
    motor_thread.running=False
    mymovehub.stop()
