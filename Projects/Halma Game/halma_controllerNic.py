# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Toro
"""

from halma_model import HalmaModel
from halma_view_gui_class import HalmaViewGUI
# from halma_player import HalmaPlayer
from halma_player1 import HalmaPlayer1 # Basic Random AI 1
# from halma_player2 import HalmaPlayer2 # Smart AI 2

# Build the Object
model = HalmaModel()
layar = HalmaViewGUI()
p1 = HalmaPlayer1("AMBIS")
p2 = HalmaPlayer1("GENIUS")

# Render pieces for normal 2 Player Game
layar.startNormalGame()

print(p1.nama)
print(p2.nama)

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

# # Main Script
# def halma(p1, p2):
#     valid = model.S_OK  # =1
#     model.awal(p1, p2)
#     layar.tampilAwal(model)
#     while (valid == model.S_OK):
#         model.mainMulai()
#         layar.tampilMulai(model)
#         g = model.getGiliran()
#         p = model.getPemain(g)
#         aksi, asal, tujuan = p.main(model)
#         selesai = model.getWaktu()
#         if (aksi == model.A_LONCAT):
#             for xy in tujuan:
#                 valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
#                 if (valid == model.S_OK):
#                     layar.tampilLoncat(asal[0], asal[1], xy[0], xy[1])
#         elif (aksi == model.A_GESER):
#             valid = model.mainGeser(
#                 asal[0], asal[1], tujuan[0][0], tujuan[0][1])
#             if (valid == model.S_OK):
#                 layar.tampilGeser(asal[0], asal[1], tujuan[0], tujuan[1])
#         else:
#             layar.tampilHenti(model)
#         if model.akhir():
#             break
#         valid = model.ganti(selesai)
#         if valid:
#             layar.tampilGanti(model)
#     layar.tampilAkhir(model, valid)

# # Run the game
# halma(p1, p2)
