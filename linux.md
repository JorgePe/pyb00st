# Installing pyb00st in Linux

pyb00st requires python 3 and pygatt

As of today, my 3 linux systems already include pyhton 3:
- Ubuntu 17.04
- ev3dev
- Raspberry Pi's Raspbian

To install pygatt:

```
sudo apt-get install python3-pip
sudo pip3 install pexpect
sudo pip3 install pygatt
```

To use pyb00st:

```
mkdir pyb00st
cd pyb00st
wget https://github.com/JorgePe/pyb00st/archive/master.zip
unzip master.zip

cd pyb00st-master
export PYTHONPATH=.
./examples/demo_tilt_read.py
```

pygatt requires root privileges so when running my python script on Ubuntu and ev3dev I get
a request for sudo password. On Raspbian I don't.

I found 2 workarounds for this requirement:

        By default, scanning with gatttool requires root privileges.
        If you don't want to require root, you must add a few
        'capabilities' to your system. If you have libcap installed, run this to
        enable normal users to perform LE scanning:
            setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`
        If you do use root, the hcitool subprocess becomes more difficult to
        terminate cleanly, and may leave your Bluetooth adapter in a bad state.

so:
```
        setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool`
        setcap 'cap_net_raw,cap_net_admin+eip' `which gatttool`
```

or:
```
        sudo chmod u+s /usr/bin/hcitool
        sudo chmod u+s /usr/bin/gatttool
```

I tried both on my Ubuntu and it didn't work :(

Also I've noticed that sometimes, after a few runs my Ubuntu laptop, the HCI device gets
stalled and I need to reboot to fix it.
