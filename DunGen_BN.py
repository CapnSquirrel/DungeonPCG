from pomegranate import *
from BN_helper import decorate

size = DiscreteDistribution( { 's': 1./3, 'm': 1./3, 'l': 1./3} )

entrance = DiscreteDistribution( { '0': 0.0, '1': 0.1 } )

boss = DiscreteDistribution( { '0': 0.0, '1': 0.1 } )

exit = DiscreteDistribution( { '0': 0.0, '1': 0.1 } )

treasure_1 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

treasure_2 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

trap_1 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

trap_2 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

empty_1 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

empty_2 = ConditionalProbabilityTable(
        [[ 's', '0', 0.20 ],
         [ 's', '1', 0.80 ],
         [ 'm', '0', 0.1 ],
         [ 'm', '1', 0.9 ],
         [ 'l', '0', 0.0 ],
         [ 'l', '1', 0.1 ]], [size] )

entrance_boss = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, boss] )

entrance_exit = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, exit] )

entrance_treasure_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, treasure_1] )

entrance_treasure_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, treasure_2] )

entrance_trap_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, trap_1] )

entrance_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, trap_2] )

entrance_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, empty_1] )

entrance_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [entrance, empty_2] )

boss_exit = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, exit] )

boss_treasure_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, treasure_1] )

boss_treasure_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, treasure_2] )

boss_trap_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, trap_1] )

boss_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, trap_2] )

boss_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, empty_1] )

boss_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [boss, empty_2] )

exit_treasure_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, treasure_1] )

exit_treasure_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, treasure_2] )

exit_trap_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, trap_1] )

exit_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, trap_2] )

exit_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, empty_1] )

exit_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [exit, empty_2] )

treasure_1_treasure_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_1, treasure_2] )

treasure_1_trap_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_1, trap_1] )

treasure_1_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_1, trap_2] )

treasure_1_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_1, empty_1] )

treasure_1_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_1, empty_2] )

treasure_2_trap_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_2, trap_1] )

treasure_2_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_2, trap_2] )

treasure_2_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_2, empty_1] )

treasure_2_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [treasure_2, empty_2] )

trap_1_trap_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [trap_1, trap_2] )

trap_1_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [trap_1, empty_1] )

trap_1_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [trap_1, empty_2] )

trap_2_empty_1 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [trap_2, empty_1] )

trap_2_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [trap_2, empty_2] )

empty_1_empty_2 = ConditionalProbabilityTable(
        [[ '0', '0', '0', 1.0 ],
         [ '0', '0', '1', 0.0 ],
         [ '0', '1', '0', 1.0 ],
         [ '0', '1', '1', 0.0 ],
         [ '1', '0', '0', 1.0 ],
         [ '1', '0', '1', 1.0 ],
         [ '1', '1', '0', 0.50 ],
         [ '1', '1', '1', 0.50 ]], [empty_1, empty_2] )

Size = State( size, name="size" )
Entrance = State( entrance, name="entrance" )
Boss = State( boss, name="boss" )
Exit = State( exit, name="exit" )
Treasure_1 = State( treasure_1, name="treasure_1" )
Treasure_2 = State( treasure_2, name="treasure_2" )
Trap_1 = State( trap_1, name="trap_1" )
Trap_2 = State( trap_2, name="trap_2" )
Empty_1 = State( empty_1, name="empty_1" )
Empty_2 = State( empty_2, name="empty_2" )
Entrance_Boss = State( entrance_boss, name="entrance_boss" )
Entrance_Exit = State( entrance_exit, name="entrance_exit" )
Entrance_Treasure_1 = State( entrance_treasure_1, name="entrance_treasure_1" )
Entrance_Treasure_2 = State( entrance_treasure_2, name="entrance_treasure_2" )
Entrance_Trap_1 = State( entrance_trap_1, name="entrance_trap_1" )
Entrance_Trap_2 = State( entrance_trap_2, name="entrance_trap_2" )
Entrance_Empty_1 = State( entrance_empty_1, name="entrance_empty_1" )
Entrance_Empty_2 = State( entrance_empty_2, name="entrance_empty_2" )
Boss_Exit = State( boss_exit, name="boss_exit" )
Boss_Treasure_1 = State( boss_treasure_1, name="boss_treasure_1" )
Boss_Treasure_2 = State( boss_treasure_2, name="boss_treasure_2" )
Boss_Trap_1 = State( boss_trap_1, name="boss_trap_1" )
Boss_Trap_2 = State( boss_trap_2, name="boss_trap_2" )
Boss_Empty_1 = State( boss_empty_1, name="boss_empty_1" )
Boss_Empty_2 = State( boss_empty_2, name="boss_empty_2" )
Exit_Treasure_1 = State( exit_treasure_1, name="exit_treasure_1" )
Exit_Treasure_2 = State( exit_treasure_2, name="exit_treasure_2" )
Exit_Trap_1 = State( exit_trap_1, name="exit_trap_1" )
Exit_Trap_2 = State( exit_trap_2, name="exit_trap_2" )
Exit_Empty_1 = State( exit_empty_1, name="exit_empty_1" )
Exit_Empty_2 = State( exit_empty_2, name="exit_empty_2" )
Treasure_1_Treasure_2 = State( treasure_1_treasure_2, name="treasure_1_treasure_2" )
Treasure_1_Trap_1 = State( treasure_1_trap_1, name="treasure_1_trap_1" )
Treasure_1_Trap_2 = State( treasure_1_trap_2, name="treasure_1_trap_2" )
Treasure_1_Empty_1 = State( treasure_1_empty_1, name="treasure_1_empty_1" )
Treasure_1_Empty_2 = State( treasure_1_empty_2, name="treasure_1_empty_2" )
Treasure_2_Trap_1 = State( treasure_2_trap_1, name="treasure_2_trap_1" )
Treasure_2_Trap_2 = State( treasure_2_trap_2, name="treasure_2_trap_2" )
Treasure_2_Empty_1 = State( treasure_2_empty_1, name="treasure_2_empty_1" )
Treasure_2_Empty_2 = State( treasure_2_empty_2, name="treasure_2_empty_2" )
Trap_1_Trap_2 = State( trap_1_trap_2, name="trap_1_trap_2" )
Trap_1_Empty_1 = State( trap_1_empty_1, name="trap_1_empty_1" )
Trap_1_Empty_2 = State( trap_1_empty_2, name="trap_1_empty_2" )
Trap_2_Empty_1 = State( trap_2_empty_1, name="trap_2_empty_1" )
Trap_2_Empty_2 = State( trap_2_empty_2, name="trap_2_empty_2" )
Empty_1_Empty_2 = State( empty_1_empty_2, name="empty_1_empty_2" )

model = BayesianNetwork( "RPG Dungeon Generator" )

model.add_states(
Size,
Entrance,
Boss,
Exit,
Treasure_1,
Treasure_2,
Trap_1,
Trap_2,
Empty_1,
Empty_2,
Entrance_Boss,
Entrance_Exit,
Entrance_Treasure_1,
Entrance_Treasure_2,
Entrance_Trap_1,
Entrance_Trap_2,
Entrance_Empty_1,
Entrance_Empty_2,
Boss_Exit,
Boss_Treasure_1,
Boss_Treasure_2,
Boss_Trap_1,
Boss_Trap_2,
Boss_Empty_1,
Boss_Empty_2,
Exit_Treasure_1,
Exit_Treasure_2,
Exit_Trap_1,
Exit_Trap_2,
Exit_Empty_1,
Exit_Empty_2,
Treasure_1_Treasure_2,
Treasure_1_Trap_1,
Treasure_1_Trap_2,
Treasure_1_Empty_1,
Treasure_1_Empty_2,
Treasure_2_Trap_1,
Treasure_2_Trap_2,
Treasure_2_Empty_1,
Treasure_2_Empty_2,
Trap_1_Trap_2,
Trap_1_Empty_1,
Trap_1_Empty_2,
Trap_2_Empty_1,
Trap_2_Empty_2,
Empty_1_Empty_2)

model.add_transition(Size, Treasure_1)
model.add_transition(Size, Treasure_2)
model.add_transition(Size, Trap_1)
model.add_transition(Size, Trap_2)
model.add_transition(Size, Empty_1)
model.add_transition(Size, Empty_2)

model.add_transition(Entrance, Entrance_Boss)
model.add_transition(Entrance, Entrance_Exit)
model.add_transition(Entrance, Entrance_Treasure_1)
model.add_transition(Entrance, Entrance_Treasure_2)
model.add_transition(Entrance, Entrance_Trap_1)
model.add_transition(Entrance, Entrance_Trap_2)
model.add_transition(Entrance, Entrance_Empty_1)
model.add_transition(Entrance, Entrance_Empty_2)

model.add_transition(Boss, Entrance_Boss)
model.add_transition(Boss, Boss_Exit)
model.add_transition(Boss, Boss_Treasure_1)
model.add_transition(Boss, Boss_Treasure_2)
model.add_transition(Boss, Boss_Trap_1)
model.add_transition(Boss, Boss_Trap_2)
model.add_transition(Boss, Boss_Empty_1)
model.add_transition(Boss, Boss_Empty_2)

model.add_transition(Exit, Entrance_Exit)
model.add_transition(Exit, Boss_Exit)
model.add_transition(Exit, Exit_Treasure_1)
model.add_transition(Exit, Exit_Treasure_2)
model.add_transition(Exit, Exit_Trap_1)
model.add_transition(Exit, Exit_Trap_2)
model.add_transition(Exit, Exit_Empty_1)
model.add_transition(Exit, Exit_Empty_2)

model.add_transition(Treasure_1, Entrance_Treasure_1)
model.add_transition(Treasure_1, Boss_Treasure_1)
model.add_transition(Treasure_1, Exit_Treasure_1)
model.add_transition(Treasure_1, Treasure_1_Treasure_2)
model.add_transition(Treasure_1, Treasure_1_Trap_1)
model.add_transition(Treasure_1, Treasure_1_Trap_2)
model.add_transition(Treasure_1, Treasure_1_Empty_1)
model.add_transition(Treasure_1, Treasure_1_Empty_2)

model.add_transition(Treasure_2, Entrance_Treasure_2)
model.add_transition(Treasure_2, Boss_Treasure_2)
model.add_transition(Treasure_2, Exit_Treasure_2)
model.add_transition(Treasure_2, Treasure_1_Treasure_2)
model.add_transition(Treasure_2, Treasure_2_Trap_1)
model.add_transition(Treasure_2, Treasure_2_Trap_2)
model.add_transition(Treasure_2, Treasure_2_Empty_1)
model.add_transition(Treasure_2, Treasure_2_Empty_2)

model.add_transition(Trap_1, Entrance_Trap_1)
model.add_transition(Trap_1, Boss_Trap_1)
model.add_transition(Trap_1, Exit_Trap_1)
model.add_transition(Trap_1, Treasure_1_Trap_1)
model.add_transition(Trap_1, Treasure_2_Trap_1)
model.add_transition(Trap_1, Trap_1_Trap_2)
model.add_transition(Trap_1, Trap_1_Empty_1)
model.add_transition(Trap_1, Trap_1_Empty_2)

model.add_transition(Trap_2, Entrance_Trap_2)
model.add_transition(Trap_2, Boss_Trap_2)
model.add_transition(Trap_2, Exit_Trap_2)
model.add_transition(Trap_2, Treasure_1_Trap_2)
model.add_transition(Trap_2, Treasure_2_Trap_2)
model.add_transition(Trap_2, Trap_1_Trap_2)
model.add_transition(Trap_2, Trap_2_Empty_1)
model.add_transition(Trap_2, Trap_2_Empty_2)

model.add_transition(Empty_1, Entrance_Empty_1)
model.add_transition(Empty_1, Boss_Empty_1)
model.add_transition(Empty_1, Exit_Empty_1)
model.add_transition(Empty_1, Treasure_1_Empty_1)
model.add_transition(Empty_1, Treasure_2_Empty_1)
model.add_transition(Empty_1, Trap_1_Empty_1)
model.add_transition(Empty_1, Trap_2_Empty_1)
model.add_transition(Empty_1, Empty_1_Empty_2)

model.add_transition(Empty_2, Entrance_Empty_2)
model.add_transition(Empty_2, Boss_Empty_2)
model.add_transition(Empty_2, Exit_Empty_2)
model.add_transition(Empty_2, Treasure_1_Empty_2)
model.add_transition(Empty_2, Treasure_2_Empty_2)
model.add_transition(Empty_2, Trap_1_Empty_2)
model.add_transition(Empty_2, Trap_2_Empty_2)
model.add_transition(Empty_2, Empty_1_Empty_2)

model.bake()

# print (model.predict_proba({}))
parameters = decorate(model.predict_proba({'size': 'l'}))
# print model.predict_proba({'size': 's', 'treasure_2': '1', 'trap_2': '1', 'empty_2': '1'})
