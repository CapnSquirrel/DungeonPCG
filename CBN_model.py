# Dungeon causal Bayesian network model. Procedurally creates DAG based on given dungeon rooms and their intended behaviorself.

from CBN_node_classes import Size, Entrance, Boss, Exit, Empty, Treasure, Trap, Adjacency
import itertools

class DAG:
    def __init__(self, nodes):
        self.nodes = {'size': Size(), 'rooms': [Entrance(), Boss(), Exit()]}
        self.nodes['rooms'].extend(nodes)
        self.node_count = 0
        for k, node in self.nodes.items():
            if type(node) is list:
                for n in node:
                    self.node_count+=1
            else:
                self.node_count+=1

# automatically add the adjacency nodes and orient every node in the graph
    def populate_and_orient(self, parameters):
        nodes = self.node_count - 2 # the size node does not count toward this total and the sequence is off by 1 (one).
        adjacency_nodes = []

        # make size the parent to every room that isnt a default room
        for node in self.nodes['rooms']:
            if node.type != "Entrance" and node.type != "Boss" and node.type != "Exit":
                node.parents.append(self.nodes['size'])
                self.nodes['size'].children.append(node)

        # create adjacency nodes based on existing rooms, mark them as the children to the rooms they were created out of
        pairs = list(itertools.combinations(self.nodes['rooms'], 2))
        for pair in pairs:
            created_node = Adjacency(pair[0], pair[1])
            adjacency_nodes.append(created_node)
            pair[0].children.append(created_node)
            pair[1].children.append(created_node)

        self.nodes['adjacencies'] = adjacency_nodes



    def write(self, entry):
        if entry is "all":
            for k, item in self.nodes.items():
                if type(item) is list:
                    for node in item:
                        node.write()
                else:
                    item.write()
        else:
            for node in self.nodes[entry]:
                node.write()

# Only instantiate non-default rooms (Treasure, Trap, Empty). Minimum requirement rooms are instantiated by default.

# model = DAG([Treasure(1), Treasure(2), Trap(1), Trap(2), Empty(1), Empty(2)])
# model.populate_and_orient()
# model.write("rooms")
