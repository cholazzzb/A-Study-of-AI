from HalmaPlayer1 import HalmaPlayer1
from halma_model import HalmaModel

import time

Model = HalmaModel()

Player = HalmaPlayer1("Ambis")
Player2 = HalmaPlayer1("Genius")
Player.setNomor(1)
Player.setNomor(2)
Model.awal(Player, Player2)
Model.ganti(time.process_time())

Player2.main(Model)