import random
import time

def main():
  
  
  while 1:
    X = random.gauss(-360,360)
    Y = random.gauss(-360,360)    
    print "Current angle: " + str(X)
    print "Applied course: " + str(Y)
    time.sleep(1)
    
main()