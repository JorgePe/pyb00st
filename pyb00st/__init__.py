import sys
import os
import logging
from pathlib import Path
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class ConfigError(Exception):
    """Exception raised on errors in configuration"""
    pass

class B00stLogger:
    class __B00stLogger:
        def __init__(self):
            self.logger = logging.getLogger('pyb00st')
            self.logger.setLevel(os.getenv('PYB00ST_LOGLEVEL', 'ERROR'))
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self):
        if not B00stLogger.instance:
            B00stLogger.instance = B00stLogger.__B00stLogger()

    def __getattr__(self, name):
        return getattr(self.instance, name)

class B00stConfig:
    class __B00stConfig:
        def __init__(self):
            logger = B00stLogger().logger
            self.MY_MOVEHUB_ADD = ''
            self.MY_BTCTRLR_HCI = ''
            home = str(Path.home())
            dir_path = os.path.dirname(os.path.realpath(__file__))

            configs = [
                home + '.config/pyb00st/config.yml',
                '/etc/pyb00st/config.yml',
                dir_path + '/../etc/config.yml'
            ]
            config = 0
            for cfg_file in configs:
                logger.debug("Checking for file '%s'", cfg_file)
                if os.path.isfile(cfg_file):
                    config = cfg_file
                    break

            if config:
                stream = open(config)
                cfg = load(stream, Loader=Loader)
                for key in ('MY_MOVEHUB_ADD', 'MY_BTCTRLR_HCI'):
                    if not cfg[key]:
                        raise ConfigError("Mandatory parameter '"+key+"'"+
                                          " not found in configuration")
                    else:
                        logger.debug("Setting '%s' to '%s'" % (key, cfg[key]))
                        setattr(self, key, cfg[key])
                if cfg['LogLevel'] and not os.environ.get('PYB00ST_LOGLEVEL'):
                    logger.setLevel(cfg['LogLevel'])
            else:
                raise ConfigError("No configuration file found")
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self):
        if not B00stConfig.instance:
            B00stConfig.instance = B00stConfig.__B00stConfig()

    def __getattr__(self, name):
        return getattr(self.instance, name)
