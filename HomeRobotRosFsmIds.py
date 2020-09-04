#!/usr/bin/env python

import ConfigFile
from fsm.pysm import StateMachine, State, Event


class HomeRobotRosFsmIds:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if HomeRobotRosFsmIds.__instance is None:
            HomeRobotRosFsmIds()
        return HomeRobotRosFsmIds.__instance

    def __init__(self):
         if HomeRobotRosFsmIds.__instance is None:
        # if HomeRobotRosFsmIds.__instance is not None:
            # return HomeRobotRosFsmIds.__instance
            # raise Exception("FsmIds class is a singleton!")
        # else:
            # fsm definition
            HomeRobotRosFsmIds.__instance = self
            # define machine and states
            self.ids_state_machine = StateMachine('self.ids_state_machine')
            # define level 1 state
            ready = State('ready')
            washing = State('washing')
            cleaning = State('cleaning')
            cooking = State('cooking')
            self.ids_state_machine.add_state(ready, initial=True)
            self.ids_state_machine.add_state(washing)
            self.ids_state_machine.add_state(cleaning)
            self.ids_state_machine.add_state(cooking)
            # define transition level 1
            self.ids_state_machine.add_transition(ready, washing, events=[ConfigFile.fsm_ids_Washing_start])
            self.ids_state_machine.add_transition(ready, cleaning, events=[ConfigFile.fsm_ids_Cleaning_start])
            self.ids_state_machine.add_transition(ready, cooking,
                                                  events=[ConfigFile.fsm_ids_Cooking_start])
            # define washing level 2    state and transitions
            find_cloth = State('find_cloth')
            find_machine = State('find_machine')
            bring_cloth_to_machine = State('bring_cloth_to_machine')
            insert_cloth_to_machine = State('insert_cloth_to_machine')
            config_machine = State('config_machine')
            wash = State('wash')
            self.ids_state_machine.add_state(find_cloth)
            self.ids_state_machine.add_state(find_machine)
            self.ids_state_machine.add_state(bring_cloth_to_machine)
            self.ids_state_machine.add_state(insert_cloth_to_machine)
            self.ids_state_machine.add_state(config_machine)
            self.ids_state_machine.add_state(wash)
            self.ids_state_machine.add_transition(washing, find_cloth,
                                                  events=[ConfigFile.fsm_ids_Washing_find_cloth])
            self.ids_state_machine.add_transition(find_cloth, find_machine,
                                                  events=[ConfigFile.fsm_ids_Washing_find_machine])
            self.ids_state_machine.add_transition(find_machine, bring_cloth_to_machine,
                                                  events=[ConfigFile.fsm_ids_Washing_bring_cloth_to_machine])
            self.ids_state_machine.add_transition(bring_cloth_to_machine, insert_cloth_to_machine,
                                                  events=[ConfigFile.fsm_ids_Washing_insert_cloth_to_machine])
            self.ids_state_machine.add_transition(insert_cloth_to_machine, config_machine,
                                                  events=[ConfigFile.fsm_ids_Washing_config_machine])
            self.ids_state_machine.add_transition(config_machine, wash,
                                                  events=[ConfigFile.fsm_ids_Washing_wash])
            self.ids_state_machine.add_transition(wash, ready,
                                                  events=[ConfigFile.fsm_ids_Washing_end])
            # define cleaning level 2 state and transitions
            find_clean_tool = State('find_clean_tool')
            config_map = State('config_map')
            clean = State('clean')
            self.ids_state_machine.add_state(find_clean_tool)
            self.ids_state_machine.add_state(config_map)
            self.ids_state_machine.add_state(clean)
            self.ids_state_machine.add_transition(cleaning, find_clean_tool,
                                                  events=[ConfigFile.fsm_ids_Cleaning_find_clean_tool])
            self.ids_state_machine.add_transition(find_clean_tool, config_map,
                                                  events=[ConfigFile.fsm_ids_Cleaning_config_map])
            self.ids_state_machine.add_transition(config_map, clean, events=[ConfigFile.fsm_ids_Cleaning_clean])
            self.ids_state_machine.add_transition(clean, ready, events=[ConfigFile.fsm_ids_Cleaning_end])
            # define bring object level 2 state and transitions
            get_recipe = State('get_recipe')
            find_foodstuff = State('find_foodstuff')
            bring_foodstuff = State('bring_foodstuff')
            config_cooking_machine = State('config_cooking_machine')
            cook = State('cook')
            self.ids_state_machine.add_state(get_recipe)
            self.ids_state_machine.add_state(find_foodstuff)
            self.ids_state_machine.add_state(bring_foodstuff)
            self.ids_state_machine.add_state(config_cooking_machine)
            self.ids_state_machine.add_state(cook)
            self.ids_state_machine.add_transition(cooking, get_recipe,
                                                  events=[ConfigFile.fsm_ids_Cooking_get_recipe])
            self.ids_state_machine.add_transition(get_recipe, find_foodstuff,
                                                  events=[ConfigFile.fsm_ids_Cooking_find_foodstuff])
            self.ids_state_machine.add_transition(find_foodstuff, bring_foodstuff,
                                                  events=[ConfigFile.fsm_ids_Cooking_bring_foodstuff])
            self.ids_state_machine.add_transition(bring_foodstuff, config_cooking_machine,
                                                  events=[ConfigFile.fsm_ids_Cooking_config_cooking_machine])
            self.ids_state_machine.add_transition(config_cooking_machine, cook,
                                                  events=[ConfigFile.fsm_ids_Cooking_cook])
            self.ids_state_machine.add_transition(cook, ready,
                                                  events=[ConfigFile.fsm_ids_Cooking_end])
            # define end commands
            self.ids_state_machine.add_transition(washing, ready, events=[ConfigFile.fsm_ids_Washing_end])
            self.ids_state_machine.add_transition(cleaning, ready, events=[ConfigFile.fsm_ids_Cleaning_end])
            self.ids_state_machine.add_transition(cooking, ready, events=[ConfigFile.fsm_ids_Cooking_end])
            self.ids_state_machine.add_transition(find_cloth, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(find_machine, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(bring_cloth_to_machine, ready,
                                                  events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(insert_cloth_to_machine, ready,
                                                  events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(config_machine, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(wash, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(find_clean_tool, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(config_map, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(clean, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(get_recipe, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(find_foodstuff, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(bring_foodstuff, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(config_cooking_machine, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(config_cooking_machine, ready, events=[ConfigFile.fsm_ids_halt])
            self.ids_state_machine.add_transition(cook, ready, events=[ConfigFile.fsm_ids_halt])
            # initialization is necessary
            self.ids_state_machine.initialize()

    def submit_test_action(cls,req):
        event = req.ids_command
        print("---------\nsystem submit: '" + event + "' and ids test it based on statemachine:")
        print("befor state: " + str(HomeRobotRosFsmIds.get_instance().ids_state_machine.state))
        transition = HomeRobotRosFsmIds.get_instance().ids_state_machine._get_transition(Event(getattr(ConfigFile, event)))
        if transition:
            HomeRobotRosFsmIds.get_instance().ids_state_machine.dispatch(Event(getattr(ConfigFile, event)))
            print("after state: " + str(
                HomeRobotRosFsmIds.get_instance().ids_state_machine.state) + "\ncommand is safe")
            return 1
        else:
            print("command is not safe")
            return 0

    def reset_ids_service(cls):
        HomeRobotRosFsmIds.get_instance().ids_state_machine.dispatch(Event("halt"))
