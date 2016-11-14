import random
import time
from plane import Plane

class Symulator(object):
    """Flight simulator class"""
    def __init__(self, angle):
        self.plane = Plane(angle)
    	
    def run(self): 
        """Runs simulation"""
        while True:
            self.plane.angle = self.plane.angle - self.plane.adjustment() + self.plane.error_gauss(0,1)		
            print "Current angle: " + str(self.plane.angle)
            print "Applied correction: " + str(self.plane.adjustment())
            print "\n"
            time.sleep(1)
            
if __name__ == "__main__":
    simul = Symulator(0)
    simul.run()