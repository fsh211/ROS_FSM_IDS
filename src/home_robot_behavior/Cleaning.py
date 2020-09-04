from src import ConfigFile


class Cleaning:

    def __init__(self):
        pass

    @classmethod
    def find_clean_tool(cls):
        print(ConfigFile.behavior_Cleaning_find_clean_tool)

    @classmethod
    def config_map(cls):
        print(ConfigFile.behavior_Cleaning_config_map)

    @classmethod
    def clean(cls):
        print(ConfigFile.behavior_Cleaning_clean)

    @classmethod
    def start(cls):
        pass

    @classmethod
    def end(cls):
        pass
