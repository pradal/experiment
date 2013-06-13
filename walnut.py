from vpltkdisplay import *
from openalea.deploy.shared_data import shared_data
from openalea.plantgl.all import *

import openalea.mtg
from openalea.mtg import *
from openalea.mtg.plantframe import *

data = shared_data(openalea.mtg)

# Load walnut MTG                   
g = MTG(data/'noylum2.mtg')

dresser = plantframe.DressingData(DiameterUnit=10)
pf = plantframe.PlantFrame(g, TopDiameter='TopDia', DressingData=dresser)
PlantGL(pf.plot(gc=True))