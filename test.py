from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter
import matplotlib.pyplot as plt

import random
import trussAnalyzer
import truss

def pV(maxLoad, totalLength):
    return -1*maxLoad / totalLength
    

mesh_file = 'patch14'

bound = {0: [1, 0],
         1: [1, 1]}
             
mesh = gmsh.Parse(mesh_file)

ele = element.Data()
for i in range(23):
    ele.E[i] = 100.
    ele.A[i] = 10.
    ele.TYPE[i] = 'Truss'
    
loadNode = 8

model = structure.Builder(mesh, ele, bound) 

maxLoad = trussAnalyzer.findMaxLoad(mesh, model, ele, loadNode, 0, 10, -100)

print(maxLoad)

nodal_load = {loadNode: [0, maxLoad]}

U, Q  = displmethod.solver(mesh, model, ele, nodal_load) 

trus= truss.truss(model.XYZ, model.CON, Q)

print(trus.failed)

print(trus.totalLength)
print('Broken member: ' + str(trus.findBroken()+1))
print('Performance rating: ' + str(pV(maxLoad, trus.totalLength)))



plotter.axialforce(model, Q)
#plotter.undeformed(model)
#plotter.deformed(model, U)

plt.show()

