# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 07:23:50 2020

@author: Mursito
@author: Toro

"""

import pygame
import time

from halma_model import HalmaModel
from halma_player import HalmaPlayer
from halma_view import HalmaView

### ----- VARIABLE DECLARATION ----- ###
# Set the color variable
black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = (0, 128, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

pcolors=[red, blue, green, yellow]

class HalmaViewGui(HalmaView):

    # Constructor
    def __init__(self, title):
        super().__init__(title)
        
        self.positions = {}
        self.thePiece = 0
        self.gameStatus = False
        self.giliran = 1
        
        ### ----- INITILIAZE pygame ----- ###
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 680))
        pygame.display.set_caption(title)
    
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
        self.pieces=[]
        for i in range(4):
            s = pygame.Surface((58, 58))
            s.fill(dark_grey)
            pygame.draw.circle(s, pcolors[i], (29, 29), 25)
            self.pieces.append(s)
            
        # CREATE PLAYER INFORMATION
        self.playerInformation = pygame.Surface((400, 576))
        self.playerInformation.fill(white)
        ## Create font objects
        self.font = pygame.font.Font('freesansbold.ttf', 32) # (font file, size)
        self.fontSmall = pygame.font.Font('freesansbold.ttf', 16)
        ## Create text suface objects, 
        self.tPlayer1 = self.fontSmall.render('PLAYER1', True, green, dark_grey) #(the text, True, text colour, background color)
        self.tPlayer1Name = self.font.render('MERAH', True, red, dark_grey)
        self.tPlayer2 = self.fontSmall.render('PLAYER2', True, green, dark_grey)
        self.tPlayer2Name = self.font.render('BIRU', True, blue, dark_grey)
        self.tPlayer3 = self.fontSmall.render('PLAYER3', True, green, dark_grey) #(the text, True, text colour, background color)
        self.tPlayer3Name = self.font.render('HIJAU', True, green, dark_grey)
        self.tPlayer4 = self.fontSmall.render('PLAYER4', True, green, dark_grey)
        self.tPlayer4Name = self.font.render('KUNING', True, yellow, dark_grey)
        
        #-----#
        self.bStart = self.font.render('START', True, green, blue)
        self.bExit = self.font.render('EXIT', True, green, blue)
        ## Create rectangular border for the objects
        self.tPlayer1R = self.tPlayer1.get_rect() 
        self.tPlayer1NameR = self.tPlayer1Name.get_rect() 
        self.tPlayer2R = self.tPlayer2.get_rect() 
        self.tPlayer2NameR = self.tPlayer2Name.get_rect() 
        self.tPlayer3R = self.tPlayer3.get_rect() 
        self.tPlayer3NameR = self.tPlayer3Name.get_rect() 
        self.tPlayer4R = self.tPlayer4.get_rect() 
        self.tPlayer4NameR = self.tPlayer4Name.get_rect() 
        
        #-----#
        self.bStartR = self.bStart.get_rect()
        self.bExitR = self.bExit.get_rect()
        
        #-----#
        self.bStartR = (800, 540)
        self.bExitR = (1000, 540)
    

    def gambarPapan(self):
        self.screen.blit(self.board, (105, 60))       

    def gambarBidak(self, model):
        nkotak = model.getUkuran()
        for x in range(nkotak):
            for y in range(nkotak):
                bxy = model.getBidak(x,y)
                if (bxy > 0):
                    p = (bxy // 100) - 1
                    self.screen.blit(self.pieces[p], (105 + x*62, 60 + y*62))

    # mulai main 2 pemain
    def tampilAwal(self, model):
        super().tampilAwal(model)
        
        # CREATE PLAYER INFORMATION
        self.playerInformation = pygame.Surface((400, 576))
        self.playerInformation.fill(white)

        ## Create font objects
        self.font = pygame.font.Font('freesansbold.ttf', 32) # (font file, size)
        self.fontSmall = pygame.font.Font('freesansbold.ttf', 16)
        
        ## Create text suface objects, 
        self.tPlayer1 = self.fontSmall.render('PLAYER1', True, green, dark_grey) #(the text, True, text colour, background color)
        p = model.getPemain(0)
        self.tPlayer1Name = self.font.render(p.nama, True, red, dark_grey)
        self.tPlayer2 = self.fontSmall.render('PLAYER2', True, green, dark_grey)
        p = model.getPemain(1)
        self.tPlayer2Name = self.font.render(p.nama, True, blue, dark_grey)
        self.tPlayer3 = self.fontSmall.render('PLAYER3', True, green, dark_grey) #(the text, True, text colour, background color)
        p = model.getPemain(2)
        self.tPlayer3Name = self.font.render(p.nama, True, green, dark_grey)
        p = model.getPemain(3)
        self.tPlayer4 = self.fontSmall.render('PLAYER4', True, green, dark_grey)
        self.tPlayer4Name = self.font.render(p.nama, True, yellow, dark_grey)        

        ## Set the center of the rectangular object. 
        self.tPlayer1R = (800, 80) 
        self.tPlayer1NameR.center = (1000, 112 + 16) 
        self.tPlayer2R = (800, 144) 
        self.tPlayer2NameR.center = (1000, 176 + 16) 
        self.tPlayer3R = (800, 208) 
        self.tPlayer3NameR.center = (1000, 240 + 16) 
        self.tPlayer4R = (800, 272) 
        self.tPlayer4NameR.center = (1000, 304 + 16) 

        
        # RENDER THE GAME
        # Clear the screen
        self.screen.fill(black)
        
        self.gambarPapan()
        self.gambarBidak(model)

        # Render Player Information
        self.screen.blit(self.playerInformation, (800, 80))
        # Render the text
        self.screen.blit(self.tPlayer1, self.tPlayer1R)
        self.screen.blit(self.tPlayer1Name, self.tPlayer1NameR)
        self.screen.blit(self.tPlayer2, self.tPlayer2R)
        self.screen.blit(self.tPlayer2Name, self.tPlayer2NameR)
        self.screen.blit(self.tPlayer3, self.tPlayer3R)
        self.screen.blit(self.tPlayer3Name, self.tPlayer3NameR)
        self.screen.blit(self.tPlayer4, self.tPlayer4R)
        self.screen.blit(self.tPlayer4Name, self.tPlayer4NameR)
        self.screen.blit(self.bStart, self.bStartR)
        self.screen.blit(self.bExit, self.bExitR)
        pygame.display.update()

    # tampilkan pemain yang aktif
    def tampilMulai(self, model):
        super().tampilMulai(model)       
        ip = model.getGiliran()
        p = model.getPemain(ip)
        langkah = model.getLangkah()       
        self.tPlayerTurn = self.font.render('LANGKAH '+ str(langkah)+ " : " + p.nama, True, pcolors[ip], black)
        self.tPlayerTurnR = self.tPlayerTurn.get_rect()        
        self.tPlayerTurnR.center = (640, 30)
        self.screen.blit(self.tPlayerTurn, self.tPlayerTurnR)
            
    # tampilkan geser
    def tampilGeser(self, model, x1, y1, x2, y2):
        super().tampilGeser(model, x1, y1, x2, y2)
        self.gambarPapan()
        self.gambarBidak(model)
        pygame.display.update()

    # tampilkan loncat
    def tampilLoncat(self, model, x1, y1, x3, y3):
        super().tampilLoncat(model, x1, y1, x3, y3)
        self.gambarPapan()
        self.gambarBidak(model)
        pygame.display.update()

    # tampilkan pemain selesai aktif        
    # dan sisa waktu
    def tampilHenti(self, model):
        super().tampilHenti(model)

    # tampilkan pergantian pemain        
    def tampilGanti(self, model):
        super().tampilGanti(model)
        self.giliran = model.getGiliran()
        self.screen.blit(self.tPlayerTurn, self.tPlayerTurnR)
        pygame.display.update()

    # tampilkan game selesai
    def tampilAkhir(self, model, status):
        super().tampilAkhir(model, status)
    
