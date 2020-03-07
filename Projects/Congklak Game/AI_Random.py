class AI(object):
    'Random not null house decision'
    
    def __init__(self, board):
        self.board = board
        self.prediction = []

    # Check if there any marble in the house (1 = there is, 0 = every house is null)
    def checkHouse(player):
        # print(Game.board)
        sumNull = 0
        for i in range(0, 7):
            # print (Game.board[player-1][i])
            if Game.board[player-1][i] == 0:
                sumNull += 1
        # print(sumNull)        
        if sumNull == 7:
            # print("TRUE")
            return 0
        else:
            return 1

    # Choose random index of array that have value not zero 
    def randomValidIndex(player):
        validIndex = []
        for i in range(0,7):
            if self.board[player-1][i] != 0:
                validIndex.append(i)

        index = randint(0,len(validIndex))
        return validIndex[index] + 1

    # random valid move
    def Move():
        if checkHouse(1) == 1:
            print("")
            print("[PLAYER 1 IS MOVE]")
            decision = randomValidIndex(1)
            print("Initial Board", Game.board)
            print("decision", decision)
            Game.setTurn(1)
            Game.move(1, decision)

randomAI = AI("board")
