# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:01:11 2020

@author: Vermillord
"""

import math
from halma_model import HalmaModel
from halma_player import HalmaPlayer
from ssd import mem

class HalmaPlayer011(HalmaPlayer):
    nama = 'Barbar'
    
    def __init__(self, nama):
        self.nama = nama
    
    global prev_move
    
    def main(self, model):
        
        # Ev. Function Param
        wlompat = 0.3
        wgrup = 0.8
        wmaju = 0.4
        #wmid = 0.15
        wdist = 0.5
        warah = 0.5
        xb = 0
        yb = 0
        xb_ev = 0
        yb_ev = 0
        delta = []
        dist = 0
        asalx = 0
        asaly = 0
        tujuanx = 0
        tujuany = 0
        mid = []
        mid_dist = []
        mid_val = 0
        maju = 0
        arahx = 0
        arahy = 0
        arah = 0
        
        # Loncat/Geser rix
        pointl = []
        pointg = []
        
        # Prev Move
        memory = 15
        prev_move = mem.pm
        
        papan = model.getPapan()
        b0 = model.getPosisiBidak(self.index)
        nb = model.getJumlahBidak()
        
        if self.index == 1:
            asalx = 0
            asaly = 0
            tujuanx = 9
            tujuany = 9
        if self.index == 2:
            asalx = 9
            asaly = 9
            tujuanx = 0
            tujuany = 0
        
        for b in b0:
            xb = xb + b[0]
            yb = yb + b[1]
        
        for b in b0:
            
            # Reset Memory
            if len(prev_move) == memory:
                prev_move = []
                
            g, l = self.bisaMain(model, papan, b[0], b[1])
            #print(g, l)
            if l != []:
                for lin in l:
                    lompat = 1
                    arah = 0
                    
                    xb_ev = xb - b[0] + lin[0]
                    yb_ev = yb - b[1] + lin[1]
                    grup_dens = (((tujuanx-xb_ev/nb)**2)-((tujuany-yb_ev/nb)**2))
                    
                    delta = [(lin[0]-b[0]),(lin[1]-b[1])]
                    dist = math.sqrt(delta[0]**2 + delta[1]**2)
                    
                    maju = math.sqrt(((asalx-lin[0])**2)+((asaly-lin[1]))**2)
                    
                    arahx = lin[0]-b[0]
                    arahy = lin[1]-b[1]
                    if arahx > 0:
                        arah = arah + 0.5
                    if arahy > 0:
                        arah = arah + 0.5
                    else:
                        arah = arah - 0.5
                
                '''i = 1
                while i <= 10:
                    mid.append([(lin[0]-i),(lin[1]-i)])
                    i = i+1
                for dist_mid in mid:
                    mid_dist.append(math.sqrt(dist_mid[0]**2+dist_mid[1]**2))
                for val in mid_dist:
                    mid_val = mid_val + val'''
                
                # Ev. Function
                ev =  wmaju*maju + wlompat*lompat + wdist*dist + wgrup*grup_dens + warah*arah #- wmid*mid_val
                
                for prev in prev_move:
                    if b == prev:
                        ev = 0
                
                # To Stop Loop
                '''if lin == prev_move:
                    ev = -999'''
                
                pointl.append([ev,l,b])
                
            if g != []:
                for gin in g:
                    lompat = 0
                    arah = 0
                    
                    xb = xb - b[0] + gin[0]
                    yb = yb - b[1] + gin[1]
                    grup_dens = (((tujuanx-xb_ev/nb)**2)-((tujuany-yb_ev/nb)**2))
                    
                    delta = [(gin[0]-b[0]),(gin[1]-b[1])]
                    dist = math.sqrt(delta[0]**2 + delta[1]**2)
                    
                    maju = math.sqrt(((asalx-gin[0])**2)+((asaly-gin[1]))**2)
                    
                    arahx = gin[0]-b[0]
                    arahy = gin[1]-b[1]
                    if arahx > 0:
                        arah = arah + 0.5
                    if arahy > 0:
                        arah = arah + 0.5
                    else:
                        arah = arah - 0.5
                    
                '''i = 1
                while i <= 10:
                    mid.append([(gin[0]-i),(gin[1]-i)])
                    i = i+1
                for dist_mid in mid:
                    mid_dist.append(math.sqrt(dist_mid[0]**2+dist_mid[1]**2))
                for val in mid_dist:
                    mid_val = mid_val + val'''
                
                # Ev. Function
                ev =  wmaju*maju + wlompat*lompat + wdist*dist + wgrup*grup_dens + warah*arah #- wmid*mid_val
                
                for prev in prev_move:
                    if b == prev:
                        ev = 0
                        
                # To Stop Loop
                '''if gin == prev_move:
                    ev = -999'''
                
                pointg.append([ev,g,b])
                
            if model.getSisaWaktu() < 1:
                pointl.sort(reverse=True)
                pointg.sort(reverse=True)
                
                if pointl[0][0] > pointg[0][0]:
                    return pointl[0][1], pointl[0][2], model.A_LONCAT
                else:
                    return pointg[0][1], pointg[0][2], model.A_GESER
            
        pointl.sort(reverse=True)
        #print("hasil sort loncat",pointl)
        pointg.sort(reverse=True)
        #print("hasil sort geser",pointg)
        if pointl[0][0] > pointg[0][0]:
            print("loncat dengan gerakan:",pointl[0][1])
            #print("titik awal:",pointl[0][2])
            #print("memory:",prev_move)
            #print("x:",pointl[0][2][0])
            prev_move.append((pointl[0][2][0],pointl[0][2][1]))
            mem.pm = prev_move
            return pointl[0][1], pointl[0][2], model.A_LONCAT
        else:
            print("geser dengan gerakan:",pointg[0][1])
            #print("titik awal:",pointl[0][2])
            #print("memory:",prev_move)
            #print("x:",pointg[0][2][0])
            prev_move.append((pointg[0][2][0],pointg[0][2][1]))
            mem.pm = prev_move
            return pointg[0][1], pointg[0][2], model.A_GESER
        
        return None,None,model.A_BERHENTI
        
        