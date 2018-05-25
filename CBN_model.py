# Dungeon causal Bayesian network model. Procedurally creates DAG based on given dungeon rooms and their intended behaviorself.

from CBN_node_classes import Size, Entrance, Boss, Exit, Empty, Treasure, Trap

class DAG:
    def __init__(self, nodes):
        self.nodes = [Size(), Entrance(), Boss(), Exit()]
        self.nodes.extend(nodes)

    def populate_and_orient(self):
        return None
        # not implemented :)

    def write(self):
        for node in self.nodes:
            node.write()

# Only instantiate non-default rooms (Treasure, Trap, Empty). Minimum requirement rooms are instantiated by default.

model = DAG([Treasure(1), Trap(1), Empty(1)])
model.populate_and_orient()
model.write()
