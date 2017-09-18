# pyb00st-pygatt

Had problems with pygattlib, notifications cause segmentation faults when using
python3 version of pygattlib.

So I'm creating another version of pyb00st library, using pygatt instead of pygattlib.

pygatt tries to reach universal coverage with backends:
- on linux it uses a gatttool backend that uses system calls to BlueZ' gatttool
- on Windows / OSX it uses a BlueGiga backend that makes use of a BlueGiga adapter like the BLED112

For my idea of using BLE with MINDSTORMS EV3 (running ev3dev) pygatt has one major advantage: it
requires much less dependancies than pygattlib. But it is also slower.

Project has grown very well. Also got a BLED112 and tried on a Windows 10 VM and it also worked!
So until pygattlib is fixed I'm going forward with pygatt only.

## How to install pygatt on Linux ##

This was tested with Ubuntu 17.04 on a x64 laptop and also with ev3dev
(ev3dev jessie, kernel 4.4.78-21-ev3dev-ev3) on LEGO MINDSTORMS EV3:
- install dependencies:
  - sudo pip3 instal pexpect
- install pygatt
  - sudo pip3 install pygatt

## How to install pygatt on Windows ##

This was tested on a Windows 10 VM:
- install python for Windows (latest  python3 version, like 'python-3.6.2-amd64')
- install dependencies:
  - pip3 install nose
  - pip3 install coverage
- install pygatt:
  - pip3 install pygatt
 
 The BGAPIBackend had some problems detecting the BLED112. It is a
 [known issue](https://github.com/peplin/pygatt/issues/118) so:
 
 - I uninstalled pygatt and donwloaded source
 - edited pygatt-master\pygatt\backends\bgapip\bgapi.py
 - added `sleep(0.25)` to `start()` method, after `self._ser.close()`
 - install with `python setup.py develop`
 
 I was using release 3.1.1. There was a new release, 3.2.0, but problem keeps occurring.
 
 
