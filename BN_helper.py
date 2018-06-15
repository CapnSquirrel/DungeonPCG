import pprint

node_names = [
'Size',
'Entrance',
'Boss',
'Exit',
'Treasure_1',
'Treasure_2',
'Trap_1',
'Trap_2',
'Empty_1',
'Empty_2',
'Entrance_Boss',
'Entrance_Exit',
'Entrance_Treasure_1',
'Entrance_Treasure_2',
'Entrance_Trap_1',
'Entrance_Trap_2',
'Entrance_Empty_1',
'Entrance_Empty_2',
'Boss_Exit',
'Boss_Treasure_1',
'Boss_Treasure_2',
'Boss_Trap_1',
'Boss_Trap_2',
'Boss_Empty_1',
'Boss_Empty_2',
'Exit_Treasure_1',
'Exit_Treasure_2',
'Exit_Trap_1',
'Exit_Trap_2',
'Exit_Empty_1',
'Exit_Empty_2',
'Treasure_1_Treasure_2',
'Treasure_1_Trap_1',
'Treasure_1_Trap_2',
'Treasure_1_Empty_1',
'Treasure_1_Empty_2',
'Treasure_2_Trap_1',
'Treasure_2_Trap_2',
'Treasure_2_Empty_1',
'Treasure_2_Empty_2',
'Trap_1_Trap_2',
'Trap_1_Empty_1',
'Trap_1_Empty_2',
'Trap_2_Empty_1',
'Trap_2_Empty_2',
'Empty_1_Empty_2']

pp = pprint.PrettyPrinter(indent=2)

def decorate(input):
    decorated_list = {}
    for name, item in zip(node_names, input):
        if type(item) is str:
            decorated_list[name] = item
        else:
            decorated_list[name] = item.parameters[0]
    pp.pprint(decorated_list)
