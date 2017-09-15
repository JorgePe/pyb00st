#!/usr/bin/env python3

from pyb00st import movehub

mymovehub = movehub("00:16:53:A4:CD:7E", "hci0")
if not mymovehub.is_connected():
    print("No connection")
    mymovehub.connect()
    
print(mymovehub.getAddress())
print(mymovehub.getName())
