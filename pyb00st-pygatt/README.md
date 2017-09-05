#pyb00st-pygatt

Had problems with pygattlib, notifications cause segmentation faults when using
python3 version of pygattlib.

So I'm creating another version of pyb00st library, using pygatt instead of pygattlib.

pygatt tries to reach universal coverage with backends:
- on linux it uses a gatttool backend that uses system calls to BlueZ' gatttool
- on Windows / OSX it uses a BlueGiga backend that makes use of a BlueGiga adapter like the BLED112

For my idea of using BLE with MINDSTORMS EV3 (running ev3dev) pygatt has one major advantage: it
requires much less dependancies than pygattlib. But it is also slower.

Until pygattlib is fixed I'm going forward with pygatt.
