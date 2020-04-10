from AIclass import Piece, Board, AIvariables

### ----- BUILD THE OBJECT----- ###
# Pondering Board for heuristic
ponderBoard = Board()

# AI variable
AIVar = AIvariables()

# Piece
p101 = Piece(101, (0, 0))
p102 = Piece(102, (1, 0))
p103 = Piece(103, (0, 1))
p104 = Piece(104, (2, 0))
p105 = Piece(105, (1, 1))
p106 = Piece(106, (0, 2))
p107 = Piece(107, (3, 0))
p108 = Piece(108, (2, 1))
p109 = Piece(109, (1, 2))
p110 = Piece(110, (0, 3))
p111 = Piece(111, (4, 0))
p112 = Piece(112, (3, 1))
p113 = Piece(113, (2, 2))
p114 = Piece(114, (1, 3))
p115 = Piece(115, (0, 4))

p201 = Piece(201, (9, 9))
p202 = Piece(202, (9, 8))
p203 = Piece(203, (8, 9))
p204 = Piece(204, (9, 7))
p205 = Piece(205, (8, 8))
p206 = Piece(206, (7, 9))
p207 = Piece(207, (9, 6))
p208 = Piece(208, (8, 7))
p209 = Piece(209, (7, 8))
p210 = Piece(210, (6, 9))
p211 = Piece(211, (9, 5))
p212 = Piece(212, (8, 6))
p213 = Piece(213, (7, 7))
p214 = Piece(214, (6, 8))
p215 = Piece(215, (5, 9))

# All Piece Objects in array
def buildPieces(nomor):
    if nomor == 0:
        Pieces = [p101, p102, p103, p104, p105, p106, p107,
                  p108, p109, p110, p111, p112, p113, p114, p115]
    else:
        Pieces = [p201, p202, p203, p204, p205, p206, p207,
                   p208, p209, p210, p211, p212, p213, p214, p215]
    return Pieces

Pieces = buildPieces(0)
ponderBoard.getPiecesPositions(Pieces)
# print(ponderBoard.PiecesPositions)

ponderBoard.calculateRelativeDistance()

for i in range (len(ponderBoard.PiecesRelativeDistance)):
    print(ponderBoard.PiecesRelativeDistance[i])