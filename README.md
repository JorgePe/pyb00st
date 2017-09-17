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

Inititally, pyb00st was intended for linux only (don't give up yet, good news ahead) because it requires BlueZ with BLE
support so a recent version of linux is required.

Since I want to use it with ev3dev it also needs python3.

And, of course, a BLE controller is also required.
 
I started this project with pygattlib. It's a library that makes direct use of BlueZ and has been included
in pybluez. But since python3 version of pygattlib has problems with notifications I started to use
a different library, pygatt, that doesn't make direct use of Bluez - instead, it makes use of a *backend*.

There are two backends for pygatt:
- on linux, a gatttool backend makes system calls to BlueZ's gatttool
- on Windows and OSX, a BlueGiga backend uses the BLE stack on a BlueGiga controller like the BLED112

On linux, the gatttool backend approach results in slower performance than pygattlib. But it also requires
much less dependencies... and it works with notifications on python 3!

On Windows or OSX, you need an extra device like the BLED112, also drivers and the like. I finally got a
BLED112 and I can confirm that changing my code to use the BGAPIBackend (just one line change) my code works
on a Windows 10 Virtual Machine (by the way, Windows 10 recognizes the BLED112 so no additional drivers needed)

The old version of pyb00st based on pygattlib is still available on 'other' folder but it lacks all input methods.
If problems with nofications on python 3 gets fixed, I'll probably backport all code.

## Status: ##

The package implements:  
   - A few constants  
   - A MoveHub class with some methods, including:    
     - controlling RGB LED color  
     - controlling Interactive motors  (timed and angle)
     - reading Color Sensor   
     - reading Distance Sensor
     - reading Motor Encoders
     - reading Button  
     - reading Tilt (Basic Mode)    
     - controlling WeDo Motors - works also with old 9V and PF 1.0 motors  
     - reading WeDo 2.0 Tilt Sensor  
     - reading WeDo 2.0 Distance Sensor (missing some modes)

I've made good progress with the pygatt version and I'm almost considering this code 'beta' level,
just need to polish it a bit and make detailed tests.

**Attention**
The names of all methods will change very soon. Probaly also the names of most internal values.

## Usage ##

You need to know the Bluetooth address of your LEGO BOOST Move Hub (like "00:16:53:A4:CD:7E") and
the name of your Bluetooth controller (like "hci0").

When you instantiate a movehub object a BLE connection is created. You should not assume that this
connection is permanent so before using you should check if it exists - if not, you should reconnect.

Currently, there is no method to check the presence of external sensors, we need to define it on
our code.

## Example: ##

```
#!/usr/bin/env python3

from pyb00st import MoveHub

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")
print( mymovehub.getname() )
```
See also 'examples' folder on source code tree.

## Roadmap ##

- Keep reading the [python styling guide](https://www.python.org/dev/peps/pep-0008/).
- Add some input and output methods:
  - battery (still not understood)
  - read enconder of port group A+B
  - deactivate sensors
  - check BLE connection (tricky)
  - read tilt in full mode
  - read ambient light level
- Improve all methods
- Keep learning python :)
- Exception handling, multithreading and all that black magic
