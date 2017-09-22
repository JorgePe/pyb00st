#!/usr/bin/env python3

# Sorry, this demo only works in linux
# It uses a Bluetooth Gamepad to wireless control a car
# and the Color Distance sensor (at port C) to prevent collisions
# after motor stop, you need to press Button to restart
# Video: https://youtu.be/e7BXDpAh2AQ
#
# I use a Bluetooth gamepad that is recognized by linux
# as an HID device:
# BLUETOOTH HID v1.1b Keyboard [Bluetooth Gamepad]
#
# To read the Gamepad I use evdev library
# it needs root/sudo or membership of plugdev / input
#
# ls -l /dev/input/
# crw-rw---- 1 root input 13, 64 set 21 09:25 event0
#
# On Ubuntu, adding my user to group input
# didn't work so I had to
#
# sudo chmod 777 /dev/input/event20
#
# and always repeat when the gamepad enters sleep mode
#
# can check the device with python3 -m evdev.evtest :
# 20  /dev/input/event20   Bluetooth Gamepad    34:f3:9a:88:60:7a
#
# I think BlueZ backend doesn't work when HCI controller already
# paired with the gamepad so you need multiple HCI controllers
# or one HCI controller and a BlueGiga adapter
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

emergency_stop = False


class MotorsThread(threading.Thread):

    right_dc = 0
    left_dc = 0

    def __init__(self):
        self.running = True
        threading.Thread.__init__(self)
        print("Motor Thread Ready")

    def run(self):
        global emergency_stop

        while self.running:
            if not emergency_stop:
                if self.left_dc != 0:
                    mymovehub.run_motor_for_time(MOTOR_B, 200, self.left_dc)
                if self.right_dc != 0:
                    mymovehub.run_motor_for_time(MOTOR_A, 200, self.right_dc)
                if self.left_dc != 0 or self.right_dc != 0:
                    sleep(0.2)


class SensorsThread(threading.Thread):

    def __init__(self):
        self.running = True
        threading.Thread.__init__(self)
        print('Distance Thread Ready')

    def run(self):
        global emergency_stop

        while self.running:
            if emergency_stop:
                if mymovehub.last_button == BUTTON_PRESSED:
                    emergency_stop = False
                    print('Restart')

            else:
                distance = mymovehub.last_distance_C
                print('Distance: ', distance)
                if distance != '' and distance < 6:
                    print('Stop!')
                    emergency_stop = True

            sleep(0.1)

#
# Find Bluetooth Gamepad
#


gamepad_found = False
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    if device.name == MY_GAMEPAD_NAME:
        my_gamepad = evdev.InputDevice(device.fn)
        gamepad_found = True

if not gamepad_found:
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
    mymovehub.subscribe_all()
    mymovehub.listen_colordist_sensor(PORT_C)
    mymovehub.listen_button()

    sensors_thread = SensorsThread()
    sensors_thread.setDaemon(True)
    sensors_thread.start()

    motors_thread = MotorsThread()
    motors_thread.setDaemon(True)
    motors_thread.start()

    for event in my_gamepad.read_loop():
        # print(event)
        if event.type == 3:
            # joystick or pad event

            # Y in [0..255] where 0 = max front, 128 = middle, 255 = max back
            if event.code == 0:
                # left.joystick,  X
                pass

            if event.code == 1:
                # left.joystick,  Y
                MotorsThread.left_dc = int((event.value - 128) / 1.28)

            if event.code == 5:
                # right joystick, Y
                MotorsThread.right_dc = int((event.value - 128) / 1.28)

            if event.code == 2:
                # right joystick, X
                pass

finally:
    motors_thread.running = False
    sensors_thread.running = False
    mymovehub.stop()
