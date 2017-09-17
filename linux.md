# Running in Linux

pygatt requires root privileges. On Ubuntu and ev3dev it asks for sudo.

From pygatt source code I found 2 workarounds:

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

Or:
```
        sudo chmod u+s /usr/bin/hcitool
        sudo chmod u+s /usr/bin/gatttool
```

I tried both and it didn't work.

Also I've noticed that after a few runs my HCI device gets stalled and I need to
reboot to fix it.
