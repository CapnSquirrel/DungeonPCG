# Class definitions for every node type in the CBN

class Node:
    def __init__(self):
        self.type = "Generic"
        self.children = []
        self.parents = []

    def write(self):
        print('..........')
        try:
            print(self.type, self.id)
        except AttributeError:
            print(self.type)

        parents = ''
        for p in self.parents:
            parents += f'{p.type} '
        print("parents:", parents)
        children = ''
        for c in self.children:
            children += f'{c.type} '
        print("children:", children)

class Size(Node):
    def __init__(self):
        self.type = "Size"
        self.children = []
        self.parents = []

class Entrance(Node):
    def __init__(self):
        self.type = "Entrance"
        self.children = []
        self.parents = []

class Boss(Node):
    def __init__(self):
        self.type = "Boss"
        self.children = []
        self.parents = []

class Exit(Node):
    def __init__(self):
        self.type = "Exit"
        self.children = []
        self.parents = []

class Empty(Node):
    def __init__(self, id):
        self.type = "Empty"
        self.id = id
        self.children = []
        self.parents = []

class Treasure(Node):
    def __init__(self, id):
        self.type = "Treasure"
        self.id = id
        self.children = []
        self.parents = []

class Trap(Node):
    def __init__(self, id):
        self.type = "Trap"
        self.id = id
        self.children = []
        self.parents = []

class Adjacency(Node):
    def __init__(self, room1, room2):
        self.type = f'{room1.type} + {room2.type}'
        self.children = []
        self.parents = []
