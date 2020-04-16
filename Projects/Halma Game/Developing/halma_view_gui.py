# -*- coding: utf-8 -*-
"""
Created on Mon March 16 15:39:50 2020
Last Update :

Halma Board Game UI

@author: Toro
"""

### ----- IMPORT MODULE ----- ###
from halma_model import HalmaModel
from halma_player import HalmaPlayer

import pygame

### ----- INITILIAZE pygame ----- ###
pygame.init()

# Configure the Screen width and height
screen = pygame.display.set_mode((1280, 680))
# set the pygame window name 
pygame.display.set_caption('HALMA GAME') 


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
positions = {
    101: (0,0),
    102: (1,0),
    103: (0,1),
    104: (2,0),
    105: (1,1),

    106: (0,2),
    107: (3,0),
    108: (2,1),
    109: (1,2),
    110: (0,3),

    111: (4,0),
    112: (3,1),
    113: (2,2),
    114: (1,3),
    115: (0,4),       

    201: (9,9),
    202: (9,8),
    203: (8,9),
    204: (9,7),
    205: (8,8),

    206: (7,9),
    207: (9,6),
    208: (8,7),
    209: (7,8),
    210: (6,9),

    211: (9,5),
    212: (8,6),
    213: (7,7),
    214: (6,8),
    215: (5,9)  
}
# width and height variable


### ----- CREATE GAME OBJECTS ----- ###
# Create board with gridlines
board = pygame.Surface((616, 616))
board.fill(dark_grey)
for i in range(1, 10):
    pygame.draw.rect(board, grey, (0, i*58 + (i-1)*4, 616, 4)) # (surface, color, (posisi x, posisi y, lebar, tinggi))
    pygame.draw.rect(board, grey, (i*58 + (i-1)*4, 0, 4, 616))

# CREATE PIECES
## Create First Player Pieces (Red)
piece1 = pygame.Surface((58, 58))
piece1.fill(dark_grey)
pygame.draw.circle(piece1, red, (29, 29), 25)
## Create Second Player Pieces (Blue)
piece2 = pygame.Surface((58, 58))
piece2.fill(dark_grey)
pygame.draw.circle(piece2, blue, (29, 29), 25)

# CREATE PLAYER INFORMATION
playerInformation = pygame.Surface((400, 576))
playerInformation.fill(white)
## Create font objects
font = pygame.font.Font('freesansbold.ttf', 32) # (font file, size)
fontSmall = pygame.font.Font('freesansbold.ttf', 16)
## Create text suface objects, 
tPlayerTurn = font.render('PLAYER' + '1' + 'TURN', True, blue, green)
tPlayer1 = fontSmall.render('PLAYER1', True, green, blue) #(the text, True, text colour, background color)
tPlayer1Name = font.render('AMBIS', True, green, blue)
tPlayer1Points = fontSmall.render('PLAYER1POINTS' + '/15', True, green, blue)
tPlayer2 = fontSmall.render('PLAYER2', True, green, blue)
tPlayer2Name = font.render('GENIUS', True, green, blue)
tPlayer2Points = fontSmall.render('PLAYER2POINTS' + '/15', True, green, blue)
#-----#
bStart = font.render('START AI GAME', True, green, blue)
bExit = font.render('EXIT', True, green, blue)
## Create rectangular border for the objects
tPlayerTurnR = tPlayerTurn.get_rect()
tPlayer1R = tPlayer1.get_rect() 
tPlayer1NameR = tPlayer1Name.get_rect() 
tPlayer1PointsR = tPlayer1Points.get_rect() 
tPlayer2R = tPlayer2.get_rect() 
tPlayer2NameR = tPlayer2Name.get_rect() 
tPlayer2PointsR = tPlayer2Points.get_rect() 
#-----#
bStartR = bStart.get_rect()
bExitR = bExit.get_rect()
## Set the center of the rectangular object. 
tPlayerTurnR.center = (640, 30)
tPlayer1R = (800, 80) 
tPlayer1NameR.center = (1000, 112 + 16) 
tPlayer1PointsR = (800, 144) 
tPlayer2R = (800, 176) 
tPlayer2NameR.center = (1000, 208 + 16) 
tPlayer2PointsR = (800, 240) 
#-----#
bStartR = (800, 540)
bExitR = (1000, 540)


'''
VOID
=> Render piece into GUI

input :
player = 1(Red) or 2 (Blue)
x = x coordinate
y = y coordinate
'''
def pieceRender(player, x, y):
    if player == 1:
        thePiece = piece1
    else:
        thePiece = piece2
    screen.blit(thePiece, (105 + x*62, 60 + y*62))

'''
VOID 
=> Render all piece to GUI

this function call :
1. pieceRender function

'''
def updateRender():
    for i in range (15):
        # print('loop', i)
        piece1 = 101
        piece2 = 201
        piece1 += i
        x, y = positions[piece1]
        pieceRender(1, x, y)
        # print(piece1, x, y)
        piece2 += i
        x, y = positions[piece2]
        pieceRender(2, x, y)
        # print(piece2, x, y)


done = False
# clock = pygame.time.Clock()


## Main Function
while not done:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ## RENDER THE GAME
    # Clear the screen
    screen.fill(black)
    # Render the board
    screen.blit(board, (105, 60))
    # Render All Pieces
    updateRender()
    # Render Player Information
    screen.blit(playerInformation, (800, 80))
    ## Render the text
    screen.blit(tPlayerTurn, tPlayerTurnR)
    screen.blit(tPlayer1, tPlayer1R)
    screen.blit(tPlayer1Name, tPlayer1NameR)  
    screen.blit(tPlayer1Points, tPlayer1PointsR)
    screen.blit(tPlayer2, tPlayer2R)
    screen.blit(tPlayer2Name, tPlayer2NameR)  
    screen.blit(tPlayer2Points, tPlayer2PointsR)
    screen.blit(bStart, bStartR)
    screen.blit(bExit, bExitR)   

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