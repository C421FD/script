import logging
from Settings import SettingsHelper
from os import path


class Logger:
    __is_initialized__ = None;
    __level__ = logging.WARNING
    __file_name__ = "log.log"
    __path__ = ""

    @staticmethod
    def get_logger(name):
        if Logger.__is_initialized__ is None:
            Logger.__initialize__()

        log = logging.getLogger(name)
        log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_appender = logging.FileHandler(path.join(Logger.__path__, Logger.__file_name__))
        file_appender.setFormatter(formatter)
        log.addHandler(file_appender)

        console_appender = logging.StreamHandler()
        console_appender.setFormatter(formatter)
        log.addHandler(console_appender)

        return log

    @staticmethod
    def __initialize__():
        getter = lambda settings_name: SettingsHelper.get_settings_value_by_name(settings_name)

        path = getter("log-path")
        if path is not None:
            Logger.__path__ = path

        file_name = getter("log-filename")
        if file_name is not None:
            Logger.__path__ = file_name
