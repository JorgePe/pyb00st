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
LED_COLORS = ['OFF','PINK','PURPLE','BLUE','LIGHTBLUE','CYAN','GREEN','YELLOW','ORANGE','RED','WHITE']

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

# Commands for motors (Timed):

# Motor A, B, C, D: 12-byte commands
# Motor AB: 13-byte commands

MOTOR_TIMED_INI = b'\x0c\x01\x81'
MOTOR_TIMED_MID = b'\x11\x09'
MOTOR_TIMED_END = b'\x64\x7f\x03'

MOTORS_TIMED_INI = b'\x0d\x01\x81'
MOTORS_TIMED_MID = b'\x11\x0A'
MOTORS_TIMED_END = b'\x64\x7f\x03'



# Commands for Color Sensor
LISTEN_COLOR_SENSOR_ON_C = b'\x0a\x00\x41\x01\x08\x01\x00\x00\x00\x01'
LISTEN_COLOR_SENSOR_ON_D = b'\x0a\x00\x41\x02\x08\x01\x00\x00\x00\x01'

# Sensor Colors:
COLOR_SENSOR_COLORS = ['BLACK','','','BLUE','','GREEN','','YELLOW','','RED','WHITE']


# Commands for Distance Sensor
LISTEN_DIST_SENSOR_ON_C = b'\x0a\x00\x41\x01\x08\x01\x00\x00\x00\x01'
LISTEN_DIST_SENSOR_ON_D = b'\x0a\x00\x41\x02\x08\x01\x00\x00\x00\x01'


# Commands for Reading Encoders

LISTEN_ENCODER_ON_A = b'\x0a\x00\x41\x37\x02\x01\x00\x00\x00\x01'
LISTEN_ENCODER_ON_B = b'\x0a\x00\x41\x38\x02\x01\x00\x00\x00\x01'
LISTEN_ENCODER_ON_C = b'\x0a\x00\x41\x01\x02\x01\x00\x00\x00\x01'
LISTEN_ENCODER_ON_D = b'\x0a\x00\x41\x02\x02\x01\x00\x00\x00\x01'

# 
ENCODER_MID = 2147483648
ENCODER_MAX = 4294967296

# Commands for Reading Button
LISTEN_BUTTON = b'\x05\x00\x01\x02\x02'

BUTTON_PRESSED = '\x01'
BUTTON_RELEASED = '\x00'

