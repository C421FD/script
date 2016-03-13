import logging
from Settings import SettingsHelper
from os import path
from Log import ColoredFormatter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    __is_initialized__ = None;
    __level__ = logging.WARNING
    __file_name__ = "log.log"
    __path__ = ""
    __log = None

    @staticmethod
    def get_logger(name):
        if Logger.__is_initialized__ is None:
            Logger.__initialize__()
            Logger.__is_initialized__ = True

        instance = Logger()
        log = logging.getLogger(name)
        instance.__log = log
        log.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_appender = logging.FileHandler(path.join(path.relpath(Logger.__path__), Logger.__file_name__))
        file_appender.setFormatter(file_formatter)
        log.addHandler(file_appender)
        FORMAT = "(asctime)s - [$BOLD%(name)-20s$RESET] - [%(levelname)-18s] - %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
        COLOR_FORMAT = ColoredFormatter.formatter_message(FORMAT, True)
        color_formatter = ColoredFormatter.ColoredFormatter(COLOR_FORMAT)
        console_appender = logging.StreamHandler()
        console_appender.setFormatter(color_formatter)
        log.addHandler(console_appender)

        return instance

    @staticmethod
    def __initialize__():
        getter = lambda settings_name: SettingsHelper.get_settings_value_by_name(settings_name)
        path = getter("log-path")
        if (path is not None) and (path != "current"):
            Logger.__path__ = path

        file_name = getter("log-filename")
        if file_name is not None:
            Logger.__file_name__ = file_name

    def info(self, message):
        self.__log.info(message)

    def warn(self, message):
        self.__log.warn(message)

    def debug(self, message):
        self.__log.debug(message)

    def error(self, message):
        self.__log.error(message)
