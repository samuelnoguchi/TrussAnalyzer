import length
import member
from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter


class truss:
    def __init__(self, modelXYZ, modelCON , Q):
        
        self.modelXYZ = modelXYZ
        self.modelCON = modelCON
        self.lengths = self.getlengths()
        
        self.Q = Q
        self.members = self.getmembers()
        self.failed = self.broken()
        self.totalLength = self.getTotalLength()
           
    def getlengths(self):
        lengths = []
        
        for con in self.modelCON:
            p1 = self.modelXYZ[con[0]]
            p2 = self.modelXYZ[con[1]]
            lengths.append((length.findLength(p1, p2)))
                
        return lengths   
    
    def getTotalLength(self):
        totalLength = 0
        for length in self.lengths:
            totalLength += length
        
        return totalLength    
        
    def getmembers(self):
        members = []

        for i in range(len(self.lengths)):
            members.append(member.member(self.lengths[i], self.Q[i]))
        
        return members
    
    def findBroken(self):
        broke = False
        for i in range(len(self.members)):
            if self.members[i].failed:
                return i
    
        
    def broken(self):
        broke = False
        for mem in self.members:
            if mem.failed == True:
                return True
                
        return False    
    
     
        