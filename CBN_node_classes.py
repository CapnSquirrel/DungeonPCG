# Class definitions for every node type in the CBN

class Node:
    def __init__(self):
        self.type = "Generic"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

    def __str__(self):
        return self.type
    
    def __repr__(self):
        return self.type

    def write(self):
        print("..........")
        print(self.type)

        parents = ""
        for p in self.parents:
            parents += f"{p.type} "
        print("parents:", parents)

        children = ""
        for c in self.children:
            children += f"{c.type} "
        print("children:", children)

        print("parameters:", self.parameters)

class Size(Node):
    def __init__(self):
        self.type = "Size"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Entrance(Node):
    def __init__(self):
        self.type = "Entrance"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Boss(Node):
    def __init__(self):
        self.type = "Boss"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Exit(Node):
    def __init__(self):
        self.type = "Exit"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Empty(Node):
    def __init__(self, id):
        self.type = f"Empty_{id}"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Treasure(Node):
    def __init__(self, id):
        self.type = f"Treasure_{id}"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Trap(Node):
    def __init__(self, id):
        self.type = f"Trap_{id}"
        self.children = []
        self.parents = []
        self.parameters = {}
        self.simulated = False

class Adjacency(Node):
    def __init__(self, room1, room2):
        self.type = f"{room1.type}_{room2.type}"
        self.parents = [room1, room2]
        self.parameters = {}
        self.simulated = False

    def write(self):
        print("..........")
        print(self.type)

        parents = ""
        for p in self.parents:
            parents += f"{p.type} "
        print("parents:", parents)
        print("parameters:", self.parameters)
