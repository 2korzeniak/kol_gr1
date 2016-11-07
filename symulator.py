import random
import time

class Symulator(object):
    """Flight simulator class"""
    def __init__(self, angle):
        self.angle = angle    
	
    def error_gauss(self,x,y):
        """Gauss error"""
        return random.gauss(x,y) 
        
    def adjustment(self):
		"""Angle adjustmentment"""
		return self.angle/2.0    
	
    def run(self): 
        """Runs simulation"""
        while True:
            self.angle = self.angle - self.adjustment() + self.error_gauss(0,1)		
            print "Current angle: " + str(self.angle)
            print "Applied correction: " + str(self.adjustment())
            print "\n"
            time.sleep(1)