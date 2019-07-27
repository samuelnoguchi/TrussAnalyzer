import material
import math

class member:
    def __init__(self, length, force, compressiveMult):
        
        self.force = force
        
        if self.force<0:
            self.length = length*compressiveMult
        else:
            self.length = length    
        
        self.dowel = 0.2
        
        if self.force<0:
            self.material = material.material(0.02, 0.00325*compressiveMult)
        else:
            self.material = material.material(0.02, 0.00325)    
            
        self.crit = self.Crit()
        self.failed = self.failure()
        
        
    def printMember(self):
        print('dimensions: L- ' + str(self.length) + ' W- ' + str(self.material.width) + ' T - ' + str(self.material.thickness))   
        print('internal force: ' + str(self.force))

    def Crit(self):
        if self.force < 0:
            return ['C', math.pow(math.pi, 2) * self.material.E * self.material.Iz / (math.pow(self.length,2))]
        else:
            return ['T', 99260000 * (self.material.width * self.material.thickness)]
        
    def failure(self):
        critical = self.crit
        if critical[0] == 'C':
            iForce = self.force * -1;
            if iForce > critical[1]:
                return True
            else:
                return False
        else:
            iForce = self.force
            if iForce > critical[1]:
                return True
            else:
                return False
            
               
      
        
           
        