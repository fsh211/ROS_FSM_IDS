from src import ConfigFile


class Cooking:

    def __init__(self):
        pass

    @classmethod
    def get_recipe(cls):
        print(ConfigFile.behavior_Cooking_get_recipe)

    @classmethod
    def find_foodstuff(cls):
        print(ConfigFile.behavior_Cooking_find_foodstuff)

    @classmethod
    def bring_foodstuff(cls):
        print(ConfigFile.behavior_Cooking_bring_foodstuff)

    @classmethod
    def config_cooking_machine(cls):
        print(ConfigFile.behavior_Cooking_config_cooking_machine)

    @classmethod
    def cook(cls):
        print(ConfigFile.behavior_Cooking_cook)

    @classmethod
    def start(cls):
        pass

    @classmethod
    def end(cls):
        pass
