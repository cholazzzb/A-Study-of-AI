# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:09:57 2020

@author: ywindows
@author: Vermillord
"""

import math

class mem:
    pmB=[]
    firstrunB=True
    goallB=[]
    
class HalmaPlayer01B:

    nama = "BarbarB"
    deskripsi = "Barbar StrategyB"
    #nomor = 1
    #index = 0
    papan = []
    teman = None
    
    def __init__(self, nama):
        self.nama = nama
        
    def setNomor(self, nomor):
        self.nomor = nomor
        self.index = nomor-1
    
    def setTeman(self, p1):
        self.teman = p1

    def bisaMain(self, model, papan, x1, y1):
        geser = []
        loncat = []
        ip = self.index;
        dTujuan = model.dalamTujuan(ip, x1, y1)
        for a in model.ARAH:
            x2 = x1 + a[0]
            y2 = y1 + a[1]
            #print((x2, y2), end="")
            if model.dalamPapan(x2, y2):
                if (papan[x2][y2] == 0):
                    if not dTujuan or model.dalamTujuan(ip, x2, y2):
                        geser.append((x2,y2))
                else:
                    x3 = x2 + a[0]
                    y3 = y2 + a[1]
                    #print((x3, y3), end="")
                    if model.dalamPapan(x3, y3):
                        if (papan[x3][y3] == 0):
                            if not dTujuan or model.dalamTujuan(ip, x3, y3):
                                loncat.append((x3,y3))
        return geser, loncat
        
    def main(self, model):
        print(mem.pmB)
        memory=5
        if len(mem.pmB)==memory:
            mem.pmB.pop(0)
        
        player = model.getPemain(self.index)
        tim = model.getTeman(self.index)
        papan = model.getPapan()
        b0 = model.getPosisiBidak(self.index)
        nb = model.getJumlahBidak()
        
        self.p1_goals = model.getPosisiBidak(2)
        self.p2_goals = model.getPosisiBidak(3)
        self.p3_goals = model.getPosisiBidak(0)
        self.p4_goals = model.getPosisiBidak(1)
        
        def player_goals(self, index):
            if index == 0:
                goal = self.p1_goals
            if index == 1:
                goal = self.p2_goals
            if index == 2:
                goal = self.p3_goals
            if index == 3:
                goal = self.p4_goals
            return goal
        
        if(mem.firstrunB == True):
            mem.goallB=player_goals(self,self.index)
            mem.firstrunB=False

        def eval_func(self, index, b, gl):
            
            ev = 0
            dist_val = 0
            delt_val = 0
            wdist = 1
            wdelt = 0.4
            
            def dist(z0,z1):
                #print("z0",z0)
                #print("z1",z1)
                
                return math.sqrt((z0[0]-z1[0])**2+(z0[1]-z1[1])**2)
            
            distances = [dist(b, goal) for goal in mem.goallB]
            #print(distances)
            for d in distances:
                dist_val = max(distances)
            delt_val = dist(b, gl)
            
            ev = wdist*dist_val + wdelt*delt_val
            
            return ev
        
        def pick_move(self, index, b):
            pointl = []
            pointg = []
            for b in b0:
                if (b not in mem.pmB):
                    g, l = self.bisaMain(model, papan, b[0], b[1])
                    #print("g",g)
                    #print("l",l)
                    eval_val=0
                    if l != []:
                        for lin in l:
                            eval_val = eval_val + 2*eval_func(self,index,b,lin)
                            #print("pl before",pointl)
                            pointl.append([eval_val,[lin],b])
                        
                            #print("pl",pointl)
                    eval_val=0
                    if g != []:
                        for gin in g:
                            #print("pg",pointg)
                            eval_val = eval_val + eval_func(self,index,b,gin)
                            pointg.append([eval_val,[gin],b])
                        
            pointl.sort(reverse=True)    
            pointg.sort(reverse=True)
            print("pointl",pointl[0][0])
            print("pointg",pointg[0][0])
            if pointl[0][0] > pointg[0][0]:
                #print("loncat")
                #print("pointl[0][1]",pointl[0][1])
                #print("pointl[0][2]",pointl[0][2])
                #print("model.A_LONCAT",model.A_LONCAT)
                mem.pmB.append(pointl[0][1])
                return pointl[0][1], pointl[0][2], model.A_LONCAT
            if pointg[0][0] > pointl[0][0]:
                #print("geser")
                mem.pmB.append(pointg[0][1])
                return pointg[0][1], pointg[0][2], model.A_GESER
            #print("berhenti")
            return None, None, model.A_BERHENTI
        
        return pick_move(self, self.index, b0)