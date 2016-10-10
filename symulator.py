import random
import time

class kol:
  def main(self):
    Y=0;
    while 1:
      X = random.gauss(-45,45)
      Y = Y-X    
      print "Current angle: " + str(Y)
      print "Applied course: " + str(X)
      print "\n"
      time.sleep(1)
      

a = kol()
a.main()