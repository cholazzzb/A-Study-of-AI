from halma_model import HalmaModel
from HalmaPlayer2 import HalmaPlayer3

# Default Setup
# Model = HalmaModel()
from copy import deepcopy

class Model(object):

    def __init__(self):
        self.BoardGame = [[101, 102, 104, 107, 111,  0,  0,  0,  0,  0],
                          [103, 105, 108, 112, 0,  0,  0,  0,  0,  0],
                          [106, 109, 113,  0,  0,  0,  0,  0,  0,  0],
                          [110, 114,  0,  0,  0,  0,  0,  0,  0,  0],
                          [115,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                          [0,  0,  0,  0,  0,  0,  0,  0,  0, 215],
                          [0,  0,  0,  0,  0,  0,  0,  0, 214, 210],
                          [0,  0,  0,  0,  0,  0,  0, 213, 209, 206],
                          [0,  0,  0,  0,  0,  0, 212, 208, 205, 203],
                          [0,  0,  0,  0,  0, 211, 207, 204, 202, 201]]

    def getPapan(self):
        return self.BoardGame

    def updateModel(self, move):
        print('MOVE', move)
        yold, xold = move[1]
        ynew, xnew = move[0][0]
        Piece = deepcopy(self.BoardGame[yold][xold])
        self.BoardGame[yold][xold] = 0
        self.BoardGame[ynew][xnew] = Piece 
        print('old', self.BoardGame[yold][xold])
        print('new', self.BoardGame[ynew][xnew])

Model = Model()

p1 = HalmaPlayer3("Ambis")
p2 = HalmaPlayer3('Genius')
p1.setNomor(1)
p2.setNomor(2)
# Model.awal(p1, p2)

# Change the code for testing below
for i in range(30):
    Model.updateModel(p1.main(Model))

# print(p1.main(Model))
