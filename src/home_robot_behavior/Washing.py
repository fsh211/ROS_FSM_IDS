from src import ConfigFile


class Washing:

    def __init__(self):
        pass

    @classmethod
    def find_cloth(cls):
        print(ConfigFile.behavior_Washing_find_cloth)

    @classmethod
    def find_machine(cls):
        print(ConfigFile.behavior_Washing_find_machine)

    @classmethod
    def bring_cloth_to_machine(cls):
        print(ConfigFile.behavior_Washing_bring_cloth_to_machine)

    @classmethod
    def insert_cloth_to_machine(cls):
        print(ConfigFile.behavior_Washing_insert_cloth_to_machine)

    @classmethod
    def config_machine(cls):
        print(ConfigFile.behavior_Washing_config_machine)

    @classmethod
    def wash(cls):
        print(ConfigFile.behavior_Washing_wash)

    @classmethod
    def start(cls):
        pass

    @classmethod
    def end(cls):
        pass
