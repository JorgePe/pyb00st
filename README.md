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

pyb00st is intended for linux only (don't give up yet, good news ahead) and it requires BlueZ with BLE
support so a recent version of linux is required.

Since I want to use it with ev3dev it also needs python3.

And, of course, a BLE controller is also required.
 
Currently there are two versions of pyb00st:
- pyb00st based on pygattlib
- pyb00st based on pygatt

I started this project with pygattlib. It's a library that makes direct use of BlueZ and has been included
in pybluez. But since python3 version of pygattlib has problems with notifications I started to use
a different library, pygatt, that doesn't make direct use of Bluez - instead, it makes use of a *backend*.

There are two backends for pygatt:
- on linux, a gatttool backend makes system calls to BlueZ' gatttool
- on Windows and OSX, a BlueGiga backend uses the BLE stack on a BlueGiga controller like the BLED112

On linux, the gatttool backend approach results in slower performance than pygattlib. But it also requires
much less dependencies... and it works with notifications!
On Windows or OSX, you need an extra device like the BLED112, and drivers and the like.


## Status: ##

The package implements:  
   A MoveHub class with some methods:  
   - connect()  
   - is_connected()  
   - getaddress() #somewhat silly#  
   - getname()  
   - set_led_color(color)  
   - motor_timed(motor, time_ms, dutycycle_pct)  
   - motors_timed(motorgrp, time_ms, dutycycle_pct_A, dutycycle_pct_B)  
   - color_sensor (pygatt version only)  
     
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
- Bypass [Issue#1](https://github.com/JorgePe/pyb00st/issues/1) so I can get notifications working (essential for reading sensors)
- Add methods for a few input functions
- Learn python :)
- Exception handling, multithreading and more black magic
