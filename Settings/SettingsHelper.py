from os import path

class SettingsHelper:

    __is_initialized__ = None
    __loaded_lines__ = [""]

    @staticmethod
    def get_settings_value_by_name(section_name):
        if SettingsHelper.__is_initialized__ is None:
            SettingsHelper.__is_initialized__ = True
            SettingsHelper.__initialize__()

        for line in SettingsHelper.__loaded_lines__:
            if section_name in line == True:
                return SettingsHelper.__get_settings_value__(section_name)

        return None

    @staticmethod
    def __initialize__():
        settings_file = None
        if path.isfile("@settings.txt"):
            settings_file = open("@settings.txt")
        else:
            if path.isfile(__path__.join("..", "@settings.txt")):
                settings_file = open(__path__.join("..", "@settings.txt"))

        if settings_file is None:
            return

        SettingsHelper.__loaded_lines__ = settings_file.readlines()

    @staticmethod
    def __get_settings_value__(raw_settings_value):
        parted_raw_value = raw_settings_value.split(":")
        if parted_raw_value.count() != 2:
            return None

        return parted_raw_value[1].strip()
