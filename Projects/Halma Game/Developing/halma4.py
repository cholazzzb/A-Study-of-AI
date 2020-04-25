# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Mursito
"""

import pygame
import time
import statistics
import traceback
import sys

from halma_model import HalmaModel
from halma_view_gui import HalmaViewGui
from StatisticsClass import StatisticsData

from halma_player_01_A import HalmaPlayer01A
from halma_player_01_B import HalmaPlayer01B
from halma_player_02_A import HalmaPlayer02A
from halma_player_02_B import HalmaPlayer02B
from HalmaPlayer03A import HalmaPlayer03A
from HalmaPlayer03B import HalmaPlayer03B
from halma_player_04_A import HalmaPlayer04A
from halma_player_04_B import HalmaPlayer04B

model = HalmaModel()
layar = HalmaViewGui("HALMA BEREGU")
statisticsData = StatisticsData()

DELAY_MAIN=0.1
DELAY_LONCAT=0.0

st_waktu = [[],[],[],[]]

def halma4(p1, p2, p3, p4):
    valid = model.S_OK
    model.awal(p1, p2, p3, p4)
    layar.tampilAwal(model)
    layar.tampilMulai(model, statisticsData)
    while (valid==model.S_OK):
        for event in pygame.event.get():
            mousePosition = pygame.mouse.get_pos()

            if layar.playersInformation[9].isInsideTheButton(mousePosition):
                layar.playersInformation[9].renderHover()
                layar.playersInformation[9].draw(layar.screen)
                pygame.display.update()
            else:
                layar.playersInformation[9].renderUnhover()
                layar.playersInformation[9].draw(layar.screen)
                pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if layar.playersInformation[9].isInsideTheButton(event.pos):
                    if layar.playersInformation[9].text == "PAUSE":
                        layar.playersInformation[9].updateText("START")
                    else:
                        layar.playersInformation[9].updateText("PAUSE")
            
            if event.type == pygame.QUIT:
                print("Permainan dibatalkan")
                return 

        model.mainMulai()
        layar.tampilMulai(model, statisticsData)
        g = model.getGiliran()
        p = model.getPemain(g)
        mulai = model.getWaktu()
        tujuan, asal, aksi = p.main(model)
        selesai = model.getWaktu()
        statisticsData.countAndUpdateMove(g, (tujuan, asal, aksi))
        statisticsData.countAndUpdateTime(g, (model.getLangkah() // 4 + (model.getLangkah() % 4 > 0)), (selesai-mulai))
        # catat lama permainan
        st_waktu[g].append(selesai-mulai)
        
        if (aksi == model.A_LONCAT):
            for xy in tujuan:
                valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
                if (valid == model.S_OK):
                    layar.tampilLoncat(model, asal[0], asal[1], xy[0], xy[1])
                asal = xy
                time.sleep(DELAY_LONCAT)
        elif (aksi == model.A_GESER):
            valid = model.mainGeser(asal[0], asal[1], tujuan[0][0], tujuan[0][1])
            if (valid == model.S_OK):
                layar.tampilGeser(model, asal[0], asal[1], tujuan[0][0], tujuan[0][1])        
        else:
            layar.tampilHenti(model)
        if model.akhirBeregu():
            break
        valid = model.ganti(selesai)
        if valid:
            layar.tampilGanti(model)
        time.sleep(DELAY_MAIN)
    layar.tampilAkhir(model, valid)
    
def laporStatistik():
    print("STATISTIK PERMAINAN")
    xt = model.getLangkah()/4
    print("Total putaran :", format(xt, ".2f"))
    print("Statistik \t\t1 \t2 \t3 \t4")
    
    print("Waktu rata", end="\t")
    for i in range(4):
        xt = statistics.mean(st_waktu[i])
        print(format(xt,".3f"), end="\t")

    print("\nWaktu min", end="\t")
    for i in range(4):
        xt = min(st_waktu[i])
        print(format(xt,".3f"), end="\t")

    print("\nWaktu max", end="\t")
    for i in range(4):
        xt = max(st_waktu[i])
        print(format(xt,".3f"), end="\t")
    
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                raise SystemExit

p1a=HalmaPlayer01A("REGU-01A")
p1b=HalmaPlayer01B("REGU-01B")
p2a=HalmaPlayer02A("REGU-02A")
p2b=HalmaPlayer02B("REGU-02B")
p3a=HalmaPlayer03A("Halmiezz")
p3b=HalmaPlayer03B("REGU-03B")
p4a=HalmaPlayer04A("REGU-04A")
p4b=HalmaPlayer04B("REGU-04B")

try: 
    halma4(p4a, p3a, p4b, p3b)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)    
    print(e)
    print("ERROR, game tidak selesai")
finally:
    # laporStatistik()
    pass
