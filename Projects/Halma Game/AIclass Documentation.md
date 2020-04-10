# New in Version 2

# Piece Class

attribute :
1. self.relativePosition = Piece relative position to all team pieces
[(x, y distance to #1 piece),
(x, y distance to #2 piece),
.......,]
(0,0 ) it means the distance is with the Piece itself

2. self.maxLoncat =


# Ponder Board Class

attributes:

1. self.PiecesPositions #DONE
2. self.PiecesRelativeDistance #DONE

methods :

#DONE
1. getPiecesPositions(self, Pieces):
        for Piece in Pieces:
            self.PiecesPositions.append(Piece.position)

#DONE
2. calculateRelativeDistance():
relativeDistance = []
PieceRelativeDistance = [] #(15x 14.....1) 
// I mean
/**
[[len 15]
[len 14]
[len 13]
[len 12]
...]
*/

        u = 1

        for i in range (len(self.PiecesPositions)):
            for residu in range (len(self.PiecesPositions) - u):
                x1, y1 = self.PiecesPositions[i]
                x2, y2 = self.PiecesPositions[residu + u]
                relativeDistance.append((x2-x1, y2-y1))
            self.PiecesRelativeDistance.append(relativeDistance)
            relativeDistance = []
            u += 1

// Passing all relative distance to Piece attributes
giveRelativeDistance(self, Pieces):

inversDistance = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
u = 1
for i in range (len(self.PiecesRelativeDistance)):
    for residu in range(len(self.PiecesRelativeDistance) - u):
        xi
    
    u++



# AI Class

Plan :
1. check the farthest piece
2. check the farthest piece relative position
if there is only a neighbour(one range piece from the farthest piece) from the piece, that neighbour piece g boleh gerak





Version 1
- Greedy

Version 2

''' Concept '''
Every Piece is an agent simple reflex agent + memory, 
Every Piece know what is its best move from the plan
The PonderBoard Sort every piece best move

- Flow Diagram:
a. Check the farthest Piece location
b. Make sure it has neighbour so It can jump
c. Calculate the longest Move (longestPossibleMove = LPM) 
d. Calculate how many moves that the Farthest Piece can move (Furthest Piece LongestPossibleMove FPLPM))
e. Decision

- Decision : 
If the LPM > FPLPM => Do LPM, else Do the plan

- Plan : 
a. 
b. 