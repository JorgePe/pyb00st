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
  no choice (and really, python 2 has to go some day).

And, of course, a BLE controller is also required. On linux systems, any Bluetooth 4.0 BLE device is OK
 as long as it is supported by the kernel. On other systems a BlueGiga adapter (like the BLED112) is
 required (it also works on linux, by the way).


## Supported environments ##

As I only have linux systems, most tests are done on my Ubuntu laptop (17.04, x64) and, of course, on
 MINDSTORMS EV3 running ev3dev. Ocasionally, I also test on my Raspberry Pi 3 and Pi Zero W, running
 ev3dev or Raspbian. I wrote a short tutorial on [how to install and use pyb00st on linux](https://github.com/JorgePe/pyb00st/blob/master/linux.md).

I now also test pyb00st on a Windows 10 Virtual Machine but I have  no means to test on OSX. It's supposed
 to work but that's all I can say.

On linux, the BlueZ backend approach results in slower performance than pygattlib and there seems to be a
 stability problem with the HCI controller. But it also requires much less dependencies... If this affects
 you, perhaps it's better to use the BlueGiga backend also on linux.

The old version of pyb00st based on pygattlib is still available on 'other' folder but it lacks all input
 methods and several other developments. If problems with nofications on python 3 ever gets fixed, I'll
 probably backport all code but for now is freeze.


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

I've made good progress with the pygatt version and I'm now considering this code 'beta' level,
 bull still need to polish it a bit and make detailed tests.


## Installation ##

pyb00st is far from being a full pyhton package that you can install with `pip`.

You need to download at least the files present inside the `pyb00st` folder. If you are not familliar with git
 just click the green "Clone or download" button and download the zip file.
 Extract the zip file to a folder of your choice, like `pyb00st`. And perhaps you want to add the path to this
 folder to PYTHONPATH environment variable.


## Usage ##

pyb00st implements one class: MoveHub(address, backend, controller)

`address` is the the Bluetooth address of your LEGO BOOST Move Hub (like "00:16:53:A4:CD:7E").

`backend` chooses the pygatt backend. There are 3 options: 'Auto', 'BlueZ' and 'BlueGiga'.
  - 'Auto' always tries to use the BlueGiga adapter but on linux, if no adapter is found, it reverts
 to BlueZ and uses the specified `controller`
  - 'Bluez' only works on linux ((like Ubuntu, Raspbian and ev3dev)), it uses the BlueZ backend with the
 specified `controller`
  - 'BlueGiga' uses the BlueGiga backeend with a compatible adapter and just ignores `controller`

`controller` is only required in linux with 'BlueZ' backend, it's the HCI name of the Bluetooth BLE controller
  (like 'hci0'). It's not used with 'BlueGiga' backend so just '' is enough.



When you `start()` a MoveHub object a BLE session is created from the specified controller.
 Sometimes this session doesn't succeed so you may need to retry it. And although I never saw a
 stablished connection drop, you should not assume that it is permanent.

It is possible to instantiate several MoveHub objects. as long as you have one BT BLE controller for each.
Currently, this is only possible in linux (and never tested, I only one Move Hub).

Each MoveHub object has it's own internal and external ports, associated to devices. Currently, there is
 no method to check for the presence (and addition or removal) of external devices, so we need to assume
 it on our code.

Each MoveHub has Input and Output methods to deal with each device.

We can use Output methods directly but for using Input methods we fist need to `subscribe` notifications
 that are sent from the MoveHub containing information about the devices that are currently active.


### Available methods: ###

 - General methods:
   - start()
   - stop()
   - is_connected()
   - get_address()
   - get_name()

 - Output methods:
   - run_motor_for_time(motor, time_ms, dutycycle_pct)
   - run_motors_for_time(motors, time_ms, dutycycle_pct_a, dutycycle_pct_b)
   - run_motor_for_angle(motor, angle, dutycycle_pct)
   - run_motor_for_angles(motors, angle, dutycycle_pct_a, dutycycle_pct_b)
   - motor_wedo(port, dutycycle_pct)
   - set_hublight(color)

 - Input methods:
   - subscribe_all()
   - listen_colordist_sensor(port)
   - listen_angle_sensor(port)
   - listen_button()
   - listen_hubtilt(mode)
   - listen_wedo_tilt(port, mode)
   - listen_wedo_distance(port, mode)


## Examples: ##


### Example 1 - simple connection ###

Assuming you have pyb00st files inside a folder named `pyb00st`, this example will connect to your LEGO BOOST
 Move Hub and print it's name:

```
#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *

mymovehub = MoveHub('00:16:53:A4:CD:7E', 'Auto', 'hci0')

try:
    mymovehub.start()
    print(mymovehub.get_name())

finally:
    mymovehub.stop()
```

It will also run on Windows, as long as you have a BlueGiga adapter like the BLED112. In that case, the 'hci0'
 argument is just ignored, the BGAPIBackend will autodiscovery it.

The `stop()` method closes the BLE session. With BlueGiga adapters it is absolutely required: if we don't
 instruct the BG adapter to do it, we will have to power off the Move Hub manually. On linux, the GATTool
 backend automatically closes after a timeout.


### Example 2 - simple output ###

This second example turns motor A ON for 1000 ms at 100% duty cycle, first in one direction
 then in the opposite direction - "Duty cycle" is a term used in Pulse Width Modulation, it
 can be interpreted as "power" or incorrectly as "speed":

```
#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *
from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'Auto', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.run_motor_for_time(MOTOR_A, 1000, 100)
    sleep(1)
    mymovehub.run_motor_for_time(MOTOR_A, 1000, -100)
    sleep(1)

finally:
    mymovehub.stop()
```


### Example 3 - simple input ###

This third example activates the internal tilt sensor and continuously polls its state:

```
#!/usr/bin/env python3

from pyb00st.movehub import MoveHub
from pyb00st.constants import *
from time import sleep

MY_MOVEHUB_ADD = '00:16:53:A4:CD:7E'
MY_BTCTRLR_HCI = 'hci0'

mymovehub = MoveHub(MY_MOVEHUB_ADD, 'Auto', MY_BTCTRLR_HCI)

try:
    mymovehub.start()
    mymovehub.subscribe_all()
    mymovehub.listen_hubtilt(MODE_HUBTILT_BASIC)

    while True:
        sleep(0.2)
        if mymovehub.last_hubtilt in TILT_BASIC_VALUES:
            print(TILT_BASIC_TEXT[mymovehub.last_hubtilt])

finally:
    mymovehub.stop()
```


Currently there is no way to de-activate a device or cancel a subscription.
 Will take care of that later.


## Documentation ##

I'll write some documentation later. For now, see 'examples' folder in the source code tree.


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
