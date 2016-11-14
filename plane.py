import random
import time

class Plane(object):
    """Plane class"""
    
    def __init__(self, angle):
        self.angle = angle        
        
    def error_gauss(self,x,y):
        """Gauss error"""
        return random.gauss(x,y) 
        
    def adjustment(self):
        """Angle adjustmentment"""
        return self.angle/2.0