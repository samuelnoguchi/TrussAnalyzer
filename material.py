import math

class material:
    def __init__(self, width, thickness):
        self.width = width
        self.thickness = thickness
        
        self.Iz = 1 / 12 *  width * math.pow(thickness, 3)
        self.E = 12780000000
        
        
        
        
        
        