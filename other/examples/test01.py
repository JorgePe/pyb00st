#!/usr/bin/env python3

from other.pyboost.movehub import MoveHub

mymovehub = MoveHub("00:16:53:A4:CD:7E", "hci0")
if not mymovehub.is_connected():
    print("No connection")
    mymovehub.connect()
    
print(mymovehub.getaddress())
print(mymovehub.getname())
