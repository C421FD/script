from os import path


class SettingsHelper:
    __is_initialized = None
    __file_name = "@settings.txt"
    __loaded_lines = [""]

    @staticmethod
    def get_settings_value_by_name(section_name):
        if SettingsHelper.__is_initialized is None:
            SettingsHelper.__is_initialized = True
            SettingsHelper.__initialize__()

        for line in SettingsHelper.__loaded_lines:
            if section_name in line:
                return SettingsHelper.__get_settings_value__(line)

        return None

    @staticmethod
    def __initialize__():
        settings_file = None
        if path.isfile(SettingsHelper.__file_name):
            settings_file = open(SettingsHelper.__file_name)
        else:
            if path.isfile(__path__.join("..", "")):
                settings_file = open(__path__.join("..", SettingsHelper.__file_name))

        if settings_file is None:
            return

        SettingsHelper.__loaded_lines = settings_file.readlines()

    @staticmethod
    def __get_settings_value__(raw_settings_value):
        parted_raw_value = raw_settings_value.split(":")
        if len(parted_raw_value) != 2:
            return None

        return parted_raw_value[1].strip()
