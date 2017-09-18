# pyb00st
Python for LEGO BOOST

The LEGO BOOST Move Hub is a BLE (Bluetooth Low Energy) device like the LEGO WeDo 2.0 Smart Hub
 and the Vengit SBrick which I already managed to control with the LEGO MINDSTORMS EV3 thanks to
 [pygattlib](https://bitbucket.org/OscarAcena/pygattlib), a python library for BLE.

I've been [reverse engineering the LEGO BOOST](https://github.com/JorgePe/BOOSTreveng) Move Hub
 and since I'm now officially crazy I decided to try to write a python package.

I started this project with pygattlib. It's a library that makes direct use of BlueZ and has been
 included in pybluez. But since python3 version of pygattlib has problems with notifications I
  started to use a different library, [pygatt](https://github.com/peplin/pygatt/tree/master/pygatt),
  that doesn't make direct use of Bluez - instead, it makes use of a *backend*. On linux systems
  this backend can be BlueZ (through system calls to BlueZ commands like hcitool and gattool) but on
  other systems (and probably also on linux aswell) it uses a different backend, based on BlueGiga's
  API - so a BG adapter, like BLED112, is needed.

Why did I call it pyb00st? Well, boost is a C++ library and there are already lots of python libraries
 related to it and I don't want to add the LEGO word because I don't want troubles.

By the way...


## Disclaimer: ##
LEGO and BOOST are Trademarks from The LEGO Company, which does not support (most probably doesn't
even know about) this project. And of course I'm not responsible for any damage on your LEGO BOOST
devices.


## Requirements ##

Inititally, pyb00st was intended for linux only (don't give up yet, good news ahead) because I was using a
 python library (pygattlib) that only works with BlueZ (the Linux bluetooth stack). Lately I was forced
 to use a different library and I am now using [pygatt](https://github.com/peplin/pygatt/tree/master/pygatt)
 (not pygattlib) that can also work on non-linux systems **if** a BlueGiga adapter is available.

 Python 3 is also needed. It is not a really requirement *per se* but I want to use pyb00st with
  LEGO MINDSTORMS EV3 (by running ev3dev) and since python 2 is no longer supported by the project I had
  no choice (and really, python 2 has to go some day)

And, of course, a BLE controller is also required. On linux systems, any Bluetooth 4.0 BLE device is OK
 as long as it is supported by the kernel. On other systems a BlueGiga adapter (like the BLED112) is
 required.


## Supported environments ##

As I only have linux systems, most tests will be done on my Ubuntu laptop (17.04, x64) and, of course,
 on MINDSTORMS EV3 running ev3dev. Ocasionally, I may also test on my Raspberry Pi 3 and Pi Zero W, running
 ev3dev or Raspbian.

I now also test pyb00st on a Windows 10 Virtual Machine but I have  no means to test on OSX. It's supposed
 to work but that's all I can say.

On linux, the gatttool backend approach results in slower performance than pygattlib. But it also requires
 much less dependencies... The old version of pyb00st based on pygattlib is still available on 'other' folder
 but it lacks all input methods.
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

## Usage ##

You need to know the Bluetooth address of your LEGO BOOST Move Hub (like "00:16:53:A4:CD:7E").

If you are on linux, you also need the name of your Bluetooth controller (like "hci0"). On other systems
 the controller is ignored as pygatt can autodiscover the BlueGiga controller.

When you instantiate a movehub object a BLE connection is created. Sometimes this connection never completes so
 you need to retry. And although I never saw a stablished connection drop, you should not assume that it is
 is permanent.

Currently, there is no method to check the presence of external sensors, we need to define it on
our code.

## Example: ##

```
#!/usr/bin/env python3

from pyb00st import MoveHub

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")
print( mymovehub.getname() )
```

I'll write some documentation later. For now, see 'examples' folder on source code tree.


## Roadmap ##

- Keep reading the [python styling guide](https://www.python.org/dev/peps/pep-0008/).
- Add some input and output methods:
  - battery (still not understood)
  - read enconder of port group A+B
  - deactivate sensors
  - check BLE connection (tricky)
  - read Hub tilt in full mode
  - read ambient light level
- Improve all methods
- Keep learning python :)
- Exception handling, multithreading and all that black magic
