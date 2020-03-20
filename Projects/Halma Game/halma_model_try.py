# -*- coding: utf-8 -*-
"""
Created on Mon March 16 15:39:50 2020
Last Update :

Halma Board Game UI

@author: Toro
"""

from halma_model import HalmaModel
from halma_player import HalmaPlayer

'''
Try HalmaModel
'''

Model = HalmaModel()
p1 = HalmaPlayer("Player 1")
p2 = HalmaPlayer("Player 2")

Model.awal(p1, p2)

print('getBidak (6,7)', Model.getBidak(6, 7))
print('getGiliran', Model.getGiliran())
print('getJatahWaktu (1)', Model.getJatahWaktu(1))
print('getPapan', Model.getPapan())
print('getJumlahBidak', type(Model.getJumlahBidak))

print('getPosisiBidak', Model.getPosisiBidak(103))
# Model.bolehGeser(index pemain = 0-1, yawal, xawal, yakhir, xakhir)




'''
updateUI(moveType, x0, y0, x1, y1):

VOID

input
movetype : 1 = geser, 2 = loncat
x0, y0 = posisi awal (x ke kanan, y ke bawah)
x1, y1 = posisi akhir
'''


def updateUI(moveType, x0, y0, x1, y1):
    if moveType == 1:
        print(Model.getBidak(y0, x0))
        # self.positions[Model.getBidak(y0, x0)] = (x1, y1)
        Model.mainGeser(y0, x0, y1, x1)
        print('getPapan', Model.getPapan())
    if moveType == 2:
        print(Model.getBidak(y0, x0))
        # self.positions[Model.getBidak(y0, x0)] = (x1, y1)
        Model.mainLoncat(y0, x0, y1, x1)
        print('getPapan', Model.getPapan())


updateUI(1, 4, 0, 5, 0)
updateUI(2, 2, 0, 4, 0)
