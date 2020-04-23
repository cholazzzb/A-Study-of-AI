# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Mursito
"""

import pygame
import time

from halma_model import HalmaModel
from halma_view_gui import HalmaViewGui
from halma_player import HalmaPlayer
from HalmaPlayer03A import HalmaPlayer03A
from HalmaPlayer03B import HalmaPlayer03B

model = HalmaModel()
layar = HalmaViewGui("HALMA BEREGU")

def halma4(p1, p2, p3, p4):
    valid = model.S_OK
    model.awal(p1, p2, p3, p4)
    layar.tampilAwal(model)
    model.mainMulai()
    layar.tampilMulai(model)
    while (valid==model.S_OK):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                raise SystemExit
        
        # NORMAL MODE
        g = model.getGiliran()
        p = model.getPemain(g)
        print('----- GILIRAN ', p.nomor, ' -----')
        print()
        tujuan, asal, aksi = p.main(model)
        selesai = model.getWaktu()
            
        if (aksi == model.A_LONCAT):
            for xy in tujuan:
                valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
                if (valid == model.S_OK):
                    layar.tampilLoncat(model, asal[0], asal[1], xy[0], xy[1])
                asal = xy
                # time.sleep(1)
        elif (aksi == model.A_GESER):
            valid = model.mainGeser(asal[0], asal[1], tujuan[0][0], tujuan[0][1])
            if (valid == model.S_OK):
                layar.tampilGeser(model, asal[0], asal[1], tujuan[0][0], tujuan[0][1])        
            # time.sleep(1)
        else:
            layar.tampilHenti(model)
        # if model.akhir():
        #     break
        valid = model.ganti(selesai)
        if valid:
            layar.tampilGanti(model)
        
        # TESTER MODE
        # for i in range (200):

        #     g = model.getGiliran()
        #     p = model.getPemain(g)
        #     print('----- GILIRAN ', p.nomor, ' -----')
        #     print()
        #     tujuan, asal, aksi = p.main(model)
        #     selesai = model.getWaktu()
            
        #     if (aksi == model.A_LONCAT):
        #         for xy in tujuan:
        #             valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
        #             if (valid == model.S_OK):
        #                 layar.tampilLoncat(model, asal[0], asal[1], xy[0], xy[1])
        #             asal = xy
        #             # time.sleep(0.1)
        #     elif (aksi == model.A_GESER):
        #         valid = model.mainGeser(asal[0], asal[1], tujuan[0][0], tujuan[0][1])
        #         if (valid == model.S_OK):
        #             layar.tampilGeser(model, asal[0], asal[1], tujuan[0][0], tujuan[0][1])        
        #         # time.sleep(0.1)
        #     else:
        #         layar.tampilHenti(model)
        #     if model.akhir():
        #         break
        #     valid = model.ganti(selesai)
        #     if valid:
        #         layar.tampilGanti(model)

        # time.sleep(300)
        
    layar.tampilAkhir(model, valid)
    time.sleep(5)
    pygame.quit()
        
p1=HalmaPlayer03A("REGU-01")
p2=HalmaPlayer03A("REGU-02")
p3=HalmaPlayer03A("REGU-03")
p4=HalmaPlayer03A("REGU-04")

p1.setTeman(p3)
p2.setTeman(p4)
p3.setTeman(p1)
p4.setTeman(p2)

halma4(p1, p2, p3, p4)

