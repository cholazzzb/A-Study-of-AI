from halma_model import HalmaModel
from HalmaPlayer2 import HalmaPlayer3

# Default Setup
Model = HalmaModel()

p1=HalmaPlayer3("Ambis")
p2=HalmaPlayer3('Genius')
p1.setNomor(1)
p2.setNomor(2)
Model.awal(p1, p2)

# Change the code for testing below
p1.main(Model)