from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter
import matplotlib.pyplot as plt

import random
import trussAnalyzer
import truss



mesh_file = 'patch12'

bound = {0: [1, 0],
         1: [1, 1]}
             
mesh = gmsh.Parse(mesh_file)




trussAnalyzer.analyzeTruss(mesh_file, bound, 5) #last parameter is loaded node





#plotter.axialforce(model, Q)
#plotter.undeformed(model)
#plotter.deformed(model, U)

plt.show()
