#Using pyb00st (pygatt version) with LEGO MINDSTORMS EV3

You need to run ev3dev (Debian Linux for MINDSTORMS EV3)

This was tested with ev3dev jessie, kernel  4.4.78-21-ev3dev-ev3

```
sudo pip3 install pygatt
```

(be patient, it takes a lot of time)

```
sudo pip3 install pexpect
mkdir github
cd github
git clone https://github.com/JorgePe/pyb00st.git
cd pyb00st
export PYTHONPATH=.
```

To run one of the examples:
```
./examples-pygatt/demo_motor-pygatt.py
```

on my case it's slow to connect to the BOOST Move Hub, I have to turn it on again while
scripts are still trying to connect.
