# Class definitions for every node type in the CBN

class Size:
    def __init__(self):
        self.type = "Size"
        self.children = None
        self.parents = None

    def write(self):
        print(self.type)

class Entrance:
    def __init__(self):
        self.type = "Entrance"
        self.children = None
        self.parents = None

    def write(self):
        print(self.type)

class Boss:
    def __init__(self):
        self.type = "Boss"
        self.children = None
        self.parents = None

    def write(self):
        print(self.type)

class Exit:
    def __init__(self):
        self.type = "Exit"
        self.children = None
        self.parents = None

    def write(self):
        print(self.type)

class Empty:
    def __init__(self, id):
        self.type = "Empty"
        self.id = id
        self.children = None
        self.parents = None

    def write(self):
        print(self.type, self.id)

class Treasure:
    def __init__(self, id):
        self.type = "Treasure"
        self.id = id
        self.children = None
        self.parents = None

    def write(self):
        print(self.type, self.id)

class Trap:
    def __init__(self, id):
        self.type = "Trap"
        self.id = id
        self.children = None
        self.parents = None

    def write(self):
        print(self.type, self.id)
