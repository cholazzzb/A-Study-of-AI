Last Update : 12 April 2020

----- AIClass.py -----

# Dependecies (Libaries) :
## From Python default
1. queue >> PriorityQueue
2. copy >> deepcopy

# Global Variables :

# There are 3 classes:
1. Piece Class => contain every Piece attributes
2. Board Class => to calculate and pondering from the real board, the ponder board can get attributes about pieces
3. AIvariables Class => contain variables for AI


## Piece Class
This class purpose is to monitor every Piece Position, Make every Piece a single agent. So The player have 15 same AI Agent

### Attributes :
1. self.player = 1 / 2 # Player 1 or 2
2. self.name = Piece name (101,.....)
3. self.position = (x, y)

------ Abai kan dulu aja 
4. self.legalMove = LegalMoves yg versi lama hanya bisa dipake pake UI versi Nic yg lama
5. self.greedyMove = bwt versi UI yg lama
6.self.range =  (xr, yr) range self.position to the destination (0,0) or (9,9)
7. self.legalMoves =  
FORMAT : 
[ 
[[[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type] ]
[[[(x2, y2)], (x1, y1), type]],
[[[(x2, y2)], (x1, y1), type], [[(x2, y2)], (x1, y1), type]]  ]

    
----- Ini yg penting
8. self.destination = (xt, yt)
9. self.newLegalMoves = []
10. self.rangeAfterMoves = []
11. self.highestRangeMove = ()

----- Abaikan lagi dulu
12.self.rangeResult = 
FORMAT :
[(xr, yr),
(xr, yr),
(xr, yr)] 
Explanation :
- The range after the best move  
- bestMove new position - destination coordinate (0,0) or (9,9)
- Smaller is better
        
13.self.deltaAverage = 
FORMAT
[(-xda, -yda),   
(-xda, -yda),
(-xda, -yda)] 
Explanation
- old Average - new Average after bestMove new Position
- Bigger is better
- (self.rangeResult - self.range) / 15


14. self.isAtDestination = False 
Explanation
- Use Boundary to check, 
- True if the piece location is in the destinantion region
15.self.bestMove = 0 
Explanation
- The Best Move Combination, 
- the index of self.legalMove
16.self.relativePosition = 
FORMAT
[(x, y distance to #1 piece),
(x, y distance to #2 piece),
.......,]
Explanation
- Piece relative position to all own team pieces
- (0,0 ) it means the distance is with the Piece itself
(Half Finished)

### Methods

1. updateAfterDecide(self, newPosition):
    Simply Update self.position to newPosition and
    update self.isAtDestiantion with boundary logic

----- Abaiin dulu aja yg ini :
(belum kepake)
2. analysisLegalMove(self):

(bwt GUI lama)
3. getBestMove(self):

4. saveLegalMove(self, legalMove):
    Simply update all move to self.legalMoves
5. clearLegalMove(self):
    Simply delete all move in self.legalMoves

----- Ini yang penting   
6. self.convertLegalMoves(self):
    Convert old Format to New Format
    return New Format
    NEW FORMAT :
    [[[(x1,y1),(x2,y2)], (x0,y0) , 1],
    [[(x1,y1),(x2,y2),(x3,y3),(x4,y4)], (x0,y0) , 1],
    [None, None , 2],
    [[(x1,y1)], (x0,y0) , 0]]

7. self.calculateRangeMoves(self):
    calculate range between position before and after the piece move

8. self.resetPieceStates(self):
    reset Most Attributes of this Piece  

9. self.switchLegalMoves(self):
    switch x and y in legal move (x = y, y = x)

    


    ##### AI VARIABLES #####
    AIvariables attributes
    1. self.directions = [(1,0), (1,-1), (0,-1),
                        (-1,-1), (-1,0), (-1,1),
                        (0,1), (1,1)]

    2. self.greedyDirections1 = [(1,0), (0,1), (1,1)]
             
    3. self.greedyDirections2 = [(-1,0), (0,-1), (-1,-1)]    
    
    4. self.finalDirections1 = [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1],
                            [0, 2], [3, 0], [2, 1], [1, 2], [0, 3], 
                            [4, 0], [3, 1], [2, 2], [1, 3], [0, 4]]
    
    5. self.finalDirections2 = [[9, 9], [8, 9], [9, 8], [7, 9], [8, 8], 
                            [9, 8], [6, 9], [7, 8], [8, 7], [9, 6], 
                            [5, 9], [8, 8], [7, 7], [8, 6], [9, 5]]

    AIvariables methods
    1.


    ##### THIS AI #####
    attributes
    self.moves = [ [[(x2, y2)], (x1, y1), type],
                [[(x2, y2)], (x1, y1), type],
                [[(x2, y2)], (x1, y1), type] ]


    methods
    1.  self.getMove(self):
    theMove = self.moves.pop(
    return theMove[0], theMove[1], theMove[2]
    )
    return [(x2, y2)], (x1, y1), type
    x2, y2 = posisi akhir
    x1, y1 = posisi awal
    type = 0=>geser, 1=>loncat, 2=> berhenti


    ##### THIS PLAYER3 #####
    main(Model):
    return best Move
    format:
    [(y2, x2)], (y1, x1), 0/1/2
    '''


## Board Class

### Attributes :

1. self.positions = {
        101: (0,0),
        102: (..),
        ...
    }

----- Abaikan dulu aja (belum / gajadi kepake)
2. self.ranges1 = (xrange, yrange) # Contain the range of total all piece player 1
3. self.ranges2 = (xrange, yrange) # idem for player 2

----- Ini penting
4. self.board = [] 
- the board from the model content all piece position
    
    
----- Abaikan dulu aja (belum / gajadi kepake)
5. self.greedyCollector = PriorityQueue()
6. self.averageRange = (xaverage, yaverage) # contain the average range from all piece of player 1 or 2 in x and y to the destination (0,0) or (9,9)
7. self.targetContainer = [False, False, .... x15]

8. self.PiecesPositions 
9. self.PiecesRelativeDistance 


----- Ini yang dipake sama AI sekarang
10. self.furthestPiece 
11. self.furthestPosition 
12. self.nearestPiece 
13. self.nearestPosition 
14. self.maxRange = (x, y)
- range between the furthest piece and nearest piece
15. self.HighestRangeOverall = (0, 0)
Explanation :
    Isinya jarak terjauh antara posisi bidak sesudah dan sebelum melangkah dari langkah pilihan
16. self.HighestRangeOverallPiece = 0
Explanation :
    Isinya adalah index Piece yang memiliki self.HighestRangeOverall
17. self.HighestRangeOverallIndex = 0
Explanation :
    Isinya adalah index langkah dari Piece yang memilki 
    self.HighestRangeOverall



### Methods :





    Ponder Board Methods
    -- OLD METHOD
    getPiece DONE
    updateBoard DONE
    updateRange DONE

    -- NEW METHOD

    1. self.updatePositions(self, pieceName, newPosition):
    

    # Get possible Geser move 1x
    2. self.getGeserMoves(self, Piece, AIvariables):
    return langkahs
    DONE

    # Get possible Loncat move 1x
    3. self.getLoncatMoves(self, Piece, AIvariables):
    return langkahs
    format:
    [ [[(x1+2, y1)], (x1, y1), type], 
      [[(x1, y1+2)], (x1, y1), type], 
      [[(x1+2, y1+2)], (x1, y1), type] ]
    DONE

    # return geser move and loncat move more than 1x
    4. self.getLegalMoves(self, Piece, AIvariables):
    return legalMoves
    format:
    [ [[[(x2, y2)], (x1, y1), type], [[(x3, y3)], (x2, y2), type], [[(x4, y4)], (x3, y3), type] ]
      [[[(x2, y2)], (x1, y1), type]],
      [[[(x2, y2)], (x1, y1), type], [[(x3, y3)], (x2, y2), type]]  ]
    DONE

    5. self.updateTargetContainer(AIVariables):
    ????? FORGET

    6. self.updateNearFarPlus(self, Pieces):
        Check the furhest and nearest piece and update the piece name and position to ponderBoard. .....
        Plus update:
        self.maxRange = self.furthestPosition - destination

    7. self.getHighestRangeMove(self, Pieces):
        return the Highest Range Move from all possible move from all owned Piece

    8. self.restartState(self):
    restart all State variable
    
    9. self.planA(self):

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


3. updateNearFar(self, Pieces):

4. planA(self):




# Algorithm
## Version 1
Take the greedy move (most jump)

## Version 2 (UNDER DEVELOPMENT)
???????
Plan :
1. check the farthest piece
2. check the farthest piece relative position
if there is only a neighbour(one range piece from the farthest piece) from the piece, that neighbour piece g boleh gerak

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

## BUG
1. Geser Move masih 1 array 










----- HalmaPlayer2New.py -----


