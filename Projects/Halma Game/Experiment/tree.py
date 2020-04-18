class Tree(object):
    def __init__(self, name):
        self.name = name
        self.child = []
    
    def setParent(self, parent):
        self.parent = parent

    def setChild(self, child):
        self.child.append(child)

MoveTree = Tree((0,0))

MoveTree.setChild(Tree((2,2)))

MoveTree.child[0].setChild(Tree((3,3)))

print(MoveTree.child[0].child[0].name)