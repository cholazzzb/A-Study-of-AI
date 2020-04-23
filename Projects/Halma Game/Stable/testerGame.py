# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Mursito
"""

import time

from halma_model import HalmaModel
from halma_view_gui import HalmaViewGui
from halma_player import HalmaPlayer
from HalmaPlayer03A import HalmaPlayer03A

model = HalmaModel()

def halma4(p1, p2, p3, p4):
    model.awal(p1, p2, p3, p4)
    p3.main(model)
        
p1=HalmaPlayer03A("REGU-01")
p2=HalmaPlayer("REGU-02")
p3=HalmaPlayer03A("REGU-03")
p4=HalmaPlayer("REGU-04")

p1.setTeman(p3)
p2.setTeman(p4)
p3.setTeman(p1)
p4.setTeman(p2)

halma4(p1, p2, p3, p4)

