# pyb00st
Python for LEGO BOOST

The LEGO BOOST Move Hub is a BLE (Bluetooth Low Energy) device like the LEGO WeDo 2.0 Smart Hub
and the Vengit SBrick which I already managed to control with the LEGO MINDSTORMS EV3 thanks to
[pygattlib](https://bitbucket.org/OscarAcena/pygattlib), a python library for BLE.

I've been [reverse engineering the LEGO BOOST](https://github.com/JorgePe/BOOSTreveng) Move Hub
and since I'm now officially crazy I decided to try to write a python package.

As the goal is to use it with ev3dev on MINDSTORMS EV3, pyb00st is ment to work only with python 3.
But since my laptop is running Ubuntu (17.04, x64) I will test pyb00st in both systems (and,
 occasionally, on my Raspberry Pi 3 and Pi Zero W running ev3dev and Raspbian)

Why did I call it pyb00st? Well, boost is a C++ library and there are already lots of python libraries related to
it and I don't want to add the LEGO word because I don't want troubles.

By the way...

## Disclaimer: ##
LEGO and BOOST are Trademarks from The LEGO Company, which does not support (most probably doesn't
even know about) this project. And of course I'm not responsible for any damage on your LEGO BOOST
devices.

## Requirements ##

pyb00st needs only python 3 and pygattlib, but since pygattlib works only on linux systems with BlueZ,
a recent version of BlueZ 5.x is required.

Of course, your hardware needs BLE support.

## Status: ##

A MoveHub classe with some methods:
- connect()
- is_connected()
- getaddress() #somewhat silly#
- getname()
- set_led_color(color)
- motor_timed(motor, time_ms, dutycycle_pct)
- motors_timed(motorgrp, time_ms, dutycycle_pct_A, dutycycle_pct_B)
Some constants.

## Usage ##

You need to know the Bluetooth address of your LEGO BOOST Move Hub (like "00:16:53:A4:CD:7E") and
the name of your Bluetooth controller (like "hci0").

When you instantiate a movehub object a BLE connection is created. You should not assume that this
connection is permanent so before using you should check if it exists - if not, you should reconnect

## Example: ##

```
#!/usr/bin/env python3

from pyb00st import MoveHub

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")
if mymovehub.is_connected() == False :
    print("No connection")
    mymovehub.connect()
    
print( mymovehub.getaddress() )
print( mymovehub.getname() )
```


## Roadmap ##

- Read the [python styling guide](https://www.python.org/dev/peps/pep-0008/).
- Add methods for all output functions (motors, RGB Led)
- Bypass Issue#1 so I can get notifications working (essential for reading sensors)
- Add methods for a few input functions
- Learn python :)
- Exception handling, multithreading and more black magic
