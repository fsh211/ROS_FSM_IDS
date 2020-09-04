# washing messages
behavior_Washing_start = 'washing start '
behavior_Washing_find_cloth = 'washing find cloth'
behavior_Washing_find_machine = 'washing find machine'
behavior_Washing_bring_cloth_to_machine = 'washing bring cloth to machine'
behavior_Washing_insert_cloth_to_machine = 'washing insert cloth to machine'
behavior_Washing_config_machine = 'washing config machine'
behavior_Washing_wash = 'washing wash'
behavior_Washing_end = 'washing end '
# cleaning messages
behavior_Cleaning_start = 'cleaning start'
behavior_Cleaning_find_clean_tool = 'cleaning find clean tool'
behavior_Cleaning_config_map = 'cleaning config map'
behavior_Cleaning_clean = 'cleaning clean'
behavior_Cleaning_end = 'cleaning end'
# cooking messages
behavior_Cooking_start = 'cooking start'
behavior_Cooking_get_recipe = 'cooking get recipe'
behavior_Cooking_find_foodstuff = 'cooking find foodstuff'
behavior_Cooking_bring_foodstuff = 'cooking bring foodstuff'
behavior_Cooking_config_cooking_machine = 'cooking config cooking machine'
behavior_Cooking_cook = 'cooking cook'
behavior_Cooking_end = 'cooking end'
# fsm ids command
fsm_ids_Washing_start = 'washing_start_command'
fsm_ids_Washing_find_cloth = 'washing_find_cloth_command'
fsm_ids_Washing_find_machine = 'washing_find_machine_command'
fsm_ids_Washing_bring_cloth_to_machine = 'washing_bring_cloth__to_machine_command'
fsm_ids_Washing_insert_cloth_to_machine = 'washing_insert_cloth__to_machine_command'
fsm_ids_Washing_config_machine = 'washing_config_machine_command'
fsm_ids_Washing_wash = 'washing_wash_command'
fsm_ids_Washing_end = 'washing_end_command'
fsm_ids_Cleaning_start = 'cleaning_start_command'
fsm_ids_Cleaning_find_clean_tool = 'cleaning_find_clean_tool_command'
fsm_ids_Cleaning_config_map = 'cleaning_config_map_command'
fsm_ids_Cleaning_clean = 'cleaning_clean_command'
fsm_ids_Cleaning_end = 'Cleaning_end_command'
fsm_ids_Cooking_start = 'cooking_start_command'
fsm_ids_Cooking_get_recipe = 'cooking_get_recipe_command'
fsm_ids_Cooking_find_foodstuff = 'cooking_find_foodstuff_command'
fsm_ids_Cooking_bring_foodstuff = 'cooking_bring_foodstuff_command'
fsm_ids_Cooking_config_cooking_machine = 'cooking_config_cooking_machine_command'
fsm_ids_Cooking_cook = 'cooking_cook_command'
fsm_ids_Cooking_end = 'cooking_end_command'
fsm_ids_halt = 'halt'
# run
level1_behavior_defined = ["Washing", "Cleaning", "Cooking"]
level2_behavior_defined = [
    "start", "end",
    "find_clean_tool", "config_map", "clean",
    "get_recipe", "find_foodstuff", "bring_foodstuff", "config_cooking_machine", "cook",
    "find_cloth", "find_machine", "bring_cloth_to_machine", "insert_cloth_to_machine", "config_machine", "wash"
]
level1_ids_enabled = "true"
level2_ids_enabled = "false"
