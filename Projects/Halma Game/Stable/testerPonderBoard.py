from AIClassTeam import PonderBoard, Piece

# TEST 1
# PASS THE TEST
# print(AIPonderBoard.piecesPosition)

# TEST 2
# PASS THE TEST
from halma_model import HalmaModel
from halma_player import HalmaPlayer

Model = HalmaModel()
p1=HalmaPlayer("REGU-01")
p2=HalmaPlayer("REGU-02")
p3=HalmaPlayer("REGU-03")
p4=HalmaPlayer("REGU-04")

p1.setTeman(p3)
p2.setTeman(p4)
p3.setTeman(p1)
p4.setTeman(p2)
Model.awal(p1, p2, p3, p4)

AIPonderBoard = PonderBoard()
AIPonderBoard.updateRealBoard(Model.getPapan())
print(AIPonderBoard.realBoard)
