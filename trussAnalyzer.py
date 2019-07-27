from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter
import truss
import random
from numpy.linalg.linalg import LinAlgError
import matplotlib.pyplot as plt

def analyzeTruss(mesh_file, bound, loadNode):
  
    #Create Geometry
    
    ele = element.Data()
    for i in range(23):
        ele.E[i] = 100.
        ele.A[i] = 10.
        ele.TYPE[i] = 'Truss'
    mesh = gmsh.Parse(mesh_file)
    model = structure.Builder(mesh, ele, bound) 
    
    trialLoad = findMaxLoad(mesh, model, ele, loadNode, 0, 10, -100)
    
    maxLoad = trialLoad
    XYZplot = model.XYZ

    for design in range(10):
    
        for coord in range(len(model.XYZ)):  
            if coord > 1 and coord != loadNode:
                model.XYZ[coord][0] = XYZplot[coord][0] + random.randint(-2,2)
                if model.XYZ[coord][0] < 0:
                    model.XYZ[coord][0] *-1
                
                model.XYZ[coord][1] = XYZplot[coord][1] + random.randint(-2,2)
            if coord == loadNode:
                model.XYZ[coord][1] = XYZplot[coord][1] + random.randint(-2,2)    
        
        try:
            trialLoad = findMaxLoad(mesh, model, ele, loadNode, 0, 10, -300)
            print(model.XYZ)
            print(trialLoad)
          
            if trialLoad < maxLoad:
                maxLoad = trialLoad
                XYZplot = model.XYZ
                print('better')
                print(XYZplot)
        
        except LinAlgError:
            continue
                
    
    print(maxLoad)        
    print(XYZplot)
    
    nodal_load = {loadNode: [0, maxLoad]}
    U, Q  = displmethod.solver(mesh, model, ele, nodal_load) 
    
    plotter.axialforce(model, Q)
    plt.show()
    
def findMaxLoad(mesh, model, ele, loadNode, start, interval, end):
    
    failed = False
    nodal_load = {loadNode: [0, start - interval]}
   
    while failed == False:    
        U, Q  = displmethod.solver(mesh, model, ele, nodal_load) 
        t = truss.truss(model.XYZ, model.CON, Q)
        
        #print(nodal_load)
        #print(t.failed)
        
        if (t.failed):
            
            if interval<=0.5:
                return nodal_load[loadNode][1]
            
            return findMaxLoad(mesh, model, ele, loadNode, nodal_load[loadNode][1]+interval, interval /2, nodal_load[loadNode][1] )
            failed =True
            
        nodal_load[loadNode][1] -= interval
        
     
    
    


   
    