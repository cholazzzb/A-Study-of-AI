# -*- coding: utf-8 -*-
"""
Created on Mon March 16 15:39:50 2020
Last Update :

Halma Board Game UI

@author: Toro
"""

### ----- IMPORT MODULE ----- ###
import pygame
import time

### ----- VARIABLE DECLARATION ----- ###
# Set the color variable
black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
# Starting position
startPositions = {
    101: (0, 0),
    102: (1, 0),
    103: (0, 1),
    104: (2, 0),
    105: (1, 1),

    106: (0, 2),
    107: (3, 0),
    108: (2, 1),
    109: (1, 2),
    110: (0, 3),

    111: (4, 0),
    112: (3, 1),
    113: (2, 2),
    114: (1, 3),
    115: (0, 4),

    201: (9, 9),
    202: (9, 8),
    203: (8, 9),
    204: (9, 7),
    205: (8, 8),

    206: (7, 9),
    207: (9, 6),
    208: (8, 7),
    209: (7, 8),
    210: (6, 9),

    211: (9, 5),
    212: (8, 6),
    213: (7, 7),
    214: (6, 8),
    215: (5, 9)
}

# Class
class HalmaViewGUI():

    # width and height variable

    # Constructor
    def __init__(self):
        self.positions = {}
        self.thePiece = 0
        
        ### ----- INITILIAZE pygame ----- ###
        pygame.init()
        # Configure the Screen width and height
        self.screen = pygame.display.set_mode((1280, 680))
        # set the pygame window name
        pygame.display.set_caption('HALMA GAME')
    
        # UI Variables
        ### ----- CREATE GAME OBJECTS ----- ###
        # Create board with gridlines
        self.board = pygame.Surface((616, 616))
        self.board.fill(dark_grey)
        for i in range(1, 10):
            pygame.draw.rect(self.board, grey, (0, i*58 + (i-1)*4, 616, 4)) # (surface, color, (posisi x, posisi y, lebar, tinggi))
            pygame.draw.rect(self.board, grey, (i*58 + (i-1)*4, 0, 4, 616))

        # CREATE PIECES
        ## Create First Player Pieces (Red)
        self.piece1 = pygame.Surface((58, 58))
        self.piece1.fill(dark_grey)
        pygame.draw.circle(self.piece1, red, (29, 29), 25)
        ## Create Second Player Pieces (Blue)
        self.piece2 = pygame.Surface((58, 58))
        self.piece2.fill(dark_grey)
        pygame.draw.circle(self.piece2, blue, (29, 29), 25)

        # CREATE PLAYER INFORMATION
        self.playerInformation = pygame.Surface((400, 576))
        self.playerInformation.fill(white)
        ## Create font objects
        self.font = pygame.font.Font('freesansbold.ttf', 32) # (font file, size)
        self.fontSmall = pygame.font.Font('freesansbold.ttf', 16)
        ## Create text suface objects, 
        self.tPlayerTurn = self.font.render('PLAYER' + '1' + 'TURN', True, blue, green)
        self.tPlayer1 = self.fontSmall.render('PLAYER1', True, green, blue) #(the text, True, text colour, background color)
        self.tPlayer1Name = self.font.render('AMBIS', True, green, blue)
        self.tPlayer1Points = self.fontSmall.render('PLAYER1POINTS' + '/15', True, green, blue)
        self.tPlayer2 = self.fontSmall.render('PLAYER2', True, green, blue)
        self.tPlayer2Name = self.font.render('GENIUS', True, green, blue)
        self.tPlayer2Points = self.fontSmall.render('PLAYER2POINTS' + '/15', True, green, blue)
        #-----#
        self.bStart = self.font.render('START AI GAME', True, green, blue)
        self.bExit = self.font.render('EXIT', True, green, blue)
        ## Create rectangular border for the objects
        self.tPlayerTurnR = self.tPlayerTurn.get_rect()
        self.tPlayer1R = self.tPlayer1.get_rect() 
        self.tPlayer1NameR = self.tPlayer1Name.get_rect() 
        self.tPlayer1PointsR = self.tPlayer1Points.get_rect() 
        self.tPlayer2R = self.tPlayer2.get_rect() 
        self.tPlayer2NameR = self.tPlayer2Name.get_rect() 
        self.tPlayer2PointsR = self.tPlayer2Points.get_rect() 
        #-----#
        self.bStartR = self.bStart.get_rect()
        self.bExitR = self.bExit.get_rect()
        ## Set the center of the rectangular object. 
        self.tPlayerTurnR.center = (640, 30)
        self.tPlayer1R = (800, 80) 
        self.tPlayer1NameR.center = (1000, 112 + 16) 
        self.tPlayer1PointsR = (800, 144) 
        self.tPlayer2R = (800, 176) 
        self.tPlayer2NameR.center = (1000, 208 + 16) 
        self.tPlayer2PointsR = (800, 240) 
        #-----#
        self.bStartR = (800, 540)
        self.bExitR = (1000, 540)

    # Build Normal 2 player game
    def buildNormalGame(self):
        self.positions = startPositions

    def updatePositions(self):
        print('Update Position')

    '''
    VOID
    => Render piece into GUI

    input :
    player = 1(Red) or 2 (Blue)
    x = x coordinate
    y = y coordinate
    '''
    def pieceRender(self, player, x, y):
        if player == 1:
            self.thePiece = self.piece1
        else:
            self.thePiece = self.piece2
        self.screen.blit(self.thePiece, (105 + x*62, 60 + y*62))

    '''
    VOID
    => Render all piece to GUI

    this function call :
    1. pieceRender function

    '''
    def updateRender(self):
        for i in range(15):
            # print('loop', i)
            firstPiece = 101
            secondPiece = 201
            firstPiece += i
            x, y = self.positions[firstPiece]
            self.pieceRender(1, x, y)
            # print(piece1, x, y)
            secondPiece += i
            x, y = self.positions[secondPiece]
            self.pieceRender(2, x, y)
            # print(piece2, x, y)


    # Infinite Loop Main Script
    def startGame(self, AI1, AI2, Controller, Model):
        print('The Game is Started')
        print(AI1.nama)
        print(AI2.nama)
        print(Controller.test())

        done = False


        ## Remember to delete this
        # Model.ganti(time.process_time())

        # clock = pygame.time.Clock()
        # Main Function
        while not done:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # RENDER THE GAME
            # Clear the screen
            self.screen.fill(black)
            # Render the board
            self.screen.blit(self.board, (105, 60))
            # Render All Pieces
            self.updateRender()
            # Render Player Information
            self.screen.blit(self.playerInformation, (800, 80))
            # Render the text
            self.screen.blit(self.tPlayerTurn, self.tPlayerTurnR)
            self.screen.blit(self.tPlayer1, self.tPlayer1R)
            self.screen.blit(self.tPlayer1Name, self.tPlayer1NameR)
            self.screen.blit(self.tPlayer1Points, self.tPlayer1PointsR)
            self.screen.blit(self.tPlayer2, self.tPlayer2R)
            self.screen.blit(self.tPlayer2Name, self.tPlayer2NameR)
            self.screen.blit(self.tPlayer2Points, self.tPlayer2PointsR)
            self.screen.blit(self.bStart, self.bStartR)
            self.screen.blit(self.bExit, self.bExitR)

            # Belum di kontrol ganti gilirannya => Menyebabkan g mau gerak bidaknya
            
            # if Model.getGiliran() == 0:
            # Giliran player 1
            decision = AI1.main(Model)
            oldY, oldX = decision[1]
            newY, newX = decision[2]
            ## Update UI
            self.positions[Model.getBidak(oldX, oldY)] = (newX, newY)
            Controller.updateModel(decision, Model)
            Model.ganti(time.process_time())
            # else:
                # Giliran player 2
            # decision = AI2.main(Model)
            # oldY, oldX = decision[1]
            # newY, newX = decision[2]
            # ## Update UI
            # self.positions[Model.getBidak(oldX, oldY)] = (newX, newY)
            # # print('hrsnya g nol', Model.getBidak(oldX, oldY))
            # Controller.updateModel(decision, Model)
            # Model.ganti(time.process_time())

            # Quit the game
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                x1 -= 1
            if keys[pygame.K_RIGHT]:
                x1 += 1
            if keys[pygame.K_UP]:
                y1 -= 1
            if keys[pygame.K_DOWN]:
                y1 += 1

            # Update the screen
            pygame.display.update()
            # clock.tick()
            # pygame.display.flip()

        pygame.quit()
