# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

Created on : 20 March 2020
Last Update : 22 March 2020

@author: Toro
"""

from halma_model import HalmaModel
from halma_view_gui_class import HalmaViewGUI
from HalmaPlayer1 import HalmaPlayer1

# from halma_player import HalmaPlayer
# from halma_player1 import HalmaPlayer1 # Basic Random AI 1
# from halma_player2 import HalmaPlayer2 # Smart AI 2
# from HalmaPlayer2 import HalmaPlayer2


class HalmaController(object):

    def __init__(self):
        self.nothing = 0

    def test(self):
        print('test')

    '''
    updateModel(decision, Model):
    decision = [moveType, (x0, y0), (x1, y1)]

    VOID 

    input
    movetype : 1 = geser, 2 = loncat
    x0, y0 = posisi awal (x ke kanan, y ke bawah)
    x1, y1 = posisi akhir
    '''
    def updateModel(self, decision, Model):
        moveType = decision[0]
        x0, y0 = decision[1]
        x1, y1 = decision[2]
        if moveType == 1:
            print('Final Decision', decision)
            # print('PapanAwal', Model.getPapan())
            # print('Kode Bidak', Model.getBidak(y0, x0))
            # self.positions[Model.getBidak(y0, x0)] = (x1, y1)
            Model.mainGeser(y0, x0, y1, x1)
            # print('PapanAkhir', Model.getPapan())
        if moveType == 2:
            print('Final Decision', decision)
            # print('PapanAwal', Model.getPapan())
            # print("Kode Bidak", Model.getBidak(y0, x0))
            # self.positions[Model.getBidak(y0, x0)] = (x1, y1)
            Model.mainLoncat(y0, x0, y1, x1)
            # print('PapanAkhir', Model.getPapan())

    def controlGame(self, Model):
        print("control Game")


# To Do : Finish Controller class and send it to GUI as parameter
# Build the Object
Model = HalmaModel()

p1 = HalmaPlayer1("AMBIS")
p2 = HalmaPlayer1("GENIUS")
p1.setNomor(1)
p2.setNomor(2)

Controller = HalmaController()

Model.awal(p1, p2)

Layar = HalmaViewGUI()

# Render pieces for normal 2 Player Game
Layar.buildNormalGame()

# Start the game
Layar.startGame(p1, p2, Controller, Model)

