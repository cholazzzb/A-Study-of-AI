Mode :

1. GreedyMode
    Move the biggestDelta
2. PlanMode
    if thereIsPieceInTheFurthestPiece:
        if thereIsNeighbourFromIdem:
            for planDirection in planDirections:
                if !neigbour3x:
                    return = Geser theNeighbourNeighbour to the direction
                else:
                    return neighbour 1 loncat 2x
        else:
            Make a third neighbour
    else:
        return geser ke yang paling banyak bisa loncat kemudian 


3. EndMode
    make a destination for a piece
    Check Jump Move
    Check Geser Move

EasyAI:

if pieceAtDestination < 10:
    if FNRange < maxDelta:
        theReturn = greedyMode()
    else:
        theReturn = planMode()
else:
    theReturn = endMode()

if theReturn[0] == None:
    theReturn = endMode()