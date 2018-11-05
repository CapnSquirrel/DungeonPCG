# Dungeon causal Bayesian network model. Procedurally creates DAG based on given dungeon rooms and their intended behaviorself.

from CBN_node_classes import Size, Entrance, Boss, Exit, Empty, Treasure, Trap, Adjacency
from DunGen_BN import model as inference_model
import BN_helper
import itertools
import numpy as np

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
        """
        populates BN with given probabilistic parameters, creates adjacency nodes for rooms marked as such,
        and orients edges for all nodes.
        """
        self.nodes['size'].parameters = parameters['Size']

        nodes = self.node_count - 2 # the size node does not count toward this total and the sequence is off by 1 (one).
        adjacency_nodes = []

        # make size the parent to every room that isnt a default room
        for node in self.nodes['rooms']:
            if node.type != "Entrance" and node.type != "Boss" and node.type != "Exit":
                node.parents.append(self.nodes['size'])
                self.nodes['size'].children.append(node)
            node.parameters = parameters[node.type]

        # create adjacency nodes based on existing rooms, mark them as the children to the rooms they were created out of
        pairs = list(itertools.combinations(self.nodes['rooms'], 2))
        for pair in pairs:
            created_node = Adjacency(pair[0], pair[1])
            created_node.parameters = parameters[created_node.type]
            adjacency_nodes.append(created_node)
            pair[0].children.append(created_node)
            pair[1].children.append(created_node)

        self.nodes['adjacencies'] = adjacency_nodes

    def topo_sort(self):
        """
        Topological sort to store each simulation step as a list of nodes.
        """

        simulations_steps = [[self.nodes['size']]]
        frontier = set()

        # add all parentless nodes to the first simulation step, these are the roots
        for node in self.nodes['rooms']:
            if not node.parents:
                simulations_steps[0].append(node)

        # add the children of the roots to the frontier
        for root in simulations_steps[0]:
            root.simulated = True
            frontier.update(root.children)

        while frontier:
            step = []
            frontier_copy = frontier.copy()
            for node in frontier_copy:
                # add to step if all parents for a node in the frontier have been simulated
                if not [True for parent in node.parents if not parent.simulated]:
                    step.append(node)
                    frontier.discard(node)
                    node.simulated = True
                    if type(node) is not Adjacency:
                        frontier.update(node.children)
            simulations_steps.append(step)
        
        return simulations_steps

    def cascade_inference(self, given):
        """
        Monte Carlo simulation for every node via graph traversal.
        """
        simulations_steps = self.topo_sort()

        updated_parameters = BN_helper.decorate(inference_model.predict_proba(given))
        for step in simulations_steps:
            for node in step:
                node.parameters = updated_parameters[node.type]
                if node.type != 'Size':
                    given[node.type.lower()] = str(np.random.choice([0,1], 1, p=list(node.parameters.values()))[0])
            updated_parameters = BN_helper.decorate(inference_model.predict_proba(given))
        
        for node in self.nodes['rooms']:
            node.parameters = updated_parameters[node.type]

        for node in self.nodes['adjacencies']:
            node.parameters = updated_parameters[node.type]
            
        return given

    def write(self, entry):
        """
        Entry is either 'all' or 'rooms', this prints either the entire BN or just the room nodes.
        """
        if entry is "all":
            for k, item in self.nodes.items():
                if type(item) is list:
                    for node in item:
                        node.write()
                else:
                    item.write()
        else:
            # other option is 'rooms'
            for node in self.nodes[entry]:
                node.write()

# Only instantiate non-default rooms (Treasure, Trap, Empty). Minimum requirement rooms are instantiated by default.

# model = DAG([Treasure(1), Treasure(2), Trap(1), Trap(2), Empty(1), Empty(2)])
# model.populate_and_orient()
# model.write("all")
