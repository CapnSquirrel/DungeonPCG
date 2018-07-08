import BN_helper
import CBN_model
from DunGen_BN import parameters
from CBN_node_classes import Size, Entrance, Boss, Exit, Empty, Treasure, Trap, Adjacency

structured_model = CBN_model.DAG([Treasure(1), Treasure(2), Trap(1), Trap(2), Empty(1), Empty(2)])
structured_model.populate_and_orient(parameters)
# structured_model.write("all")


# print(parameters)
