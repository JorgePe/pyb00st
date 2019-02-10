#!/usr/bin/python3
'''
This is an example script to demonstrate the usage of
B00stLogger and B00stConfig
'''

from pyb00st import B00stLogger
from pyb00st import B00stConfig


def get_config():
    '''This function only exists to avoid 'invalid-name' errors from pylint'''
    cfg = B00stConfig()
    log = B00stLogger().logger

    log.error("MY_MOVEHUB_ADD: %s", cfg.MY_MOVEHUB_ADD)
    log.error("MY_BTCTRLR_HCI: %s", cfg.MY_BTCTRLR_HCI)


if __name__ == "__main__":
    get_config()
