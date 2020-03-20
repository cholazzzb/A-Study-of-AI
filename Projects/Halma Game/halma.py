# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Mursito
"""

from halma_model import HalmaModel
from halma_view import HalmaView
from halma_player import HalmaPlayer

# Build the Object
model = HalmaModel()
layar = HalmaView()

def halma(p1, p2):
    valid = model.S_OK # =1
    model.awal(p1, p2)
    layar.tampilAwal(model)
    while (valid==model.S_OK):
        model.mainMulai()
        layar.tampilMulai(model)
        g = model.getGiliran()
        p = model.getPemain(g)
        aksi, asal, tujuan = p.main(model)
        selesai = model.getWaktu()
        if (aksi == model.A_LONCAT):
            for xy in tujuan:
                valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
                if (valid == model.S_OK):
                    layar.tampilLoncat(asal[0], asal[1], xy[0], xy[1])
        elif (aksi == model.A_GESER):
            valid = model.mainGeser(asal[0], asal[1], tujuan[0][0], tujuan[0][1])
            if (valid == model.S_OK):
                layar.tampilGeser(asal[0], asal[1], tujuan[0], tujuan[1])        
        else:
            layar.tampilHenti(model)
        if model.akhir():
            break
        valid = model.ganti(selesai)
        if valid:
            layar.tampilGanti(model)
    layar.tampilAkhir(model, valid)
        

p1=HalmaPlayer("Pintar")
p2=HalmaPlayer("Cerdas")

halma(p1, p2)


