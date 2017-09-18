#
# Constants
#

MOVE_HUB_HARDWARE_HANDLE = 0x0E
MOVE_HUB_HARDWARE_UUID = '00001624-1212-efde-1623-785feabcd123'

# Ports

PORT_A = 0x37
PORT_B = 0x38
PORT_C = 0x01
PORT_D = 0x02
PORT_TILT = 0x3A

# Device Types
TYPE_NONE = 0x00
TYPE_WEDO2MOTOR = 0x01
TYPE_LED = 0x17
TYPE_WEDO2TILT = 0x22
TYPE_WEDO2DISTANCE = 0x23
TYPE_COLORDISTANCE = 0x25
TYPE_ENCODERMOTOR = 0x26
TYPE_MOTOR = 0x27   # ???
TYPE_HUBTILT = 0x28


# Commands for setting RGB LED color
SET_LED_OFF = b'\x08\x00\x81\x32\x11\x51\x00\x00'
SET_LED_PINK = b'\x08\x00\x81\x32\x11\x51\x00\x01'
SET_LED_PURPLE = b'\x08\x00\x81\x32\x11\x51\x00\x02'
SET_LED_BLUE = b'\x08\x00\x81\x32\x11\x51\x00\x03'
SET_LED_LIGHTBLUE = b'\x08\x00\x81\x32\x11\x51\x00\x04'
SET_LED_CYAN = b'\x08\x00\x81\x32\x11\x51\x00\x05'
SET_LED_GREEN = b'\x08\x00\x81\x32\x11\x51\x00\x06'
SET_LED_YELLOW = b'\x08\x00\x81\x32\x11\x51\x00\x07'
SET_LED_ORANGE = b'\x08\x00\x81\x32\x11\x51\x00\x08'
SET_LED_RED = b'\x08\x00\x81\x32\x11\x51\x00\x09'
SET_LED_WHITE = b'\x08\x00\x81\x32\x11\x51\x00\x0A'

SET_LED_COLOR = [SET_LED_OFF,
                 SET_LED_PINK,
                 SET_LED_PURPLE,
                 SET_LED_BLUE,
                 SET_LED_LIGHTBLUE,
                 SET_LED_CYAN,
                 SET_LED_GREEN,
                 SET_LED_YELLOW,
                 SET_LED_ORANGE,
                 SET_LED_RED,
                 SET_LED_WHITE]

# Colors:
LED_COLORS = ['OFF', 'PINK', 'PURPLE', 'BLUE', 'LIGHTBLUE', 'CYAN', 'GREEN', 'YELLOW', 'ORANGE', 'RED', 'WHITE']

# Motors:

MOTOR_A = bytes([0x37])
MOTOR_B = bytes([0x38])
MOTOR_AB = bytes([0x39])
MOTOR_C = bytes([0x01])
MOTOR_D = bytes([0x02])

# a group of all single motors
MOTORS = [MOTOR_A, MOTOR_B, MOTOR_AB, MOTOR_C, MOTOR_D]

# a group of 1 is silly but there might be other pairs in the future
MOTOR_PAIRS = [MOTOR_AB]

# Commands for Interactive Motors (Timed):

# Motor A, B, C, D: 12-byte commands
# Motor AB: 13-byte commands

MOTOR_TIMED_INI = b'\x0c\x01\x81'
MOTOR_TIMED_MID = b'\x11\x09'
MOTOR_TIMED_END = b'\x64\x7f\x03'

MOTORS_TIMED_INI = b'\x0d\x01\x81'
MOTORS_TIMED_MID = b'\x11\x0A'
MOTORS_TIMED_END = b'\x64\x7f\x03'

# Commands for Interactive Motors (Angle):

# Motor A, B, C, D: 14-byte commands
# Motor AB: 15-byte commands

MOTOR_ANGLE_INI = b'\x0e\x01\x81'
MOTOR_ANGLE_MID = b'\x11\x0b'
MOTOR_ANGLE_END = b'\x64\x7f\x03'

MOTORS_ANGLE_INI = b'\x0f\x01\x81'
MOTORS_ANGLE_MID = b'\x11\x0c'
MOTORS_ANGLE_END = b'\x64\x7f\x03'

# Commands for WeDo Motors (just Duty Cycle):
MOTOR_WEDO_INI = b'\x08\x00\x81'
MOTOR_WEDO_MID = b'\x11\x51\x00'


# Commands that Initialize sensors in certain Modes

LISTEN_INI = b'\x0a\x00\x41'
LISTEN_END = b'\x01\x00\x00\x00\x01'
LISTEN_BUTTON = b'\x05\x00\x01\x02\x02'

MODE_COLORDIST_SENSOR = b'\x08'
MODE_ENCODER = b'\x02'
MODE_HUBTILT_BASIC = b'\x02'
MODE_HUBTILT_FULL = b'\x00'

# WeDo 2.0 Tilt Sensor modes:
# 0 = angle
# 1 = tilt
# 2 = crash
# 3 = some variation of angle
# modes 0,1,2 like WeDo 2.0 modes

MODE_WEDOTILT_ANGLE = b'\x00'
MODE_WEDOTILT_TILT = b'\x01'
MODE_WEDOTILT_CRASH = b'\x02'
MODE_WEDODIST_DISTANCE = b'\x00'

# WeDo 2.0 Distance Sensor modes:
# 0 = distance 00..0A
# 1 = increments when blocked
# 2 = distance and luminosity ?
# all continuous reading
# just using mode 0=distance

MODE_WEDODIST_1 = b'\x01'
MODE_WEDODIST_2 = b'\x02'

#
# Constants:
#

# Sensor Colors:
COLOR_SENSOR_COLORS = ['BLACK', '', '', 'BLUE', '', 'GREEN', '', 'YELLOW', '', 'RED', 'WHITE']

# Encoder
ENCODER_MID = 2147483648
ENCODER_MAX = 4294967296

# Button

BUTTON_PRESSED = '\x01'
BUTTON_RELEASED = '\x00'

# BOOST Tilt Sensor
TILT_HORIZ = 0x00
TILT_UP = 0x01
TILT_DOWN = 0x02
TILT_RIGHT = 0x03
TILT_LEFT = 0x04
TILT_INVERT = 0x05

TILT_BASIC_VALUES = [TILT_HORIZ, TILT_UP, TILT_DOWN, TILT_RIGHT, TILT_LEFT, TILT_INVERT]
TILT_BASIC_TEXT = ['TILT_HORIZ', 'TILT_UP', 'TILT_DOWN', 'TILT_RIGHT', 'TILT_LEFT', 'TILT_INVERT']

# WeDo 2.0 Tilt Sensor

WEDO_TILT_HORIZ = 0x00
WEDO_TILT_LEFT = 0x07
WEDO_TILT_RIGHT = 0x05
WEDO_TILT_UP = 0x03
WEDO_TILT_DOWN = 0x09
