import random
import time

def main():
  Y=0;
  while 1:
    X = random.gauss(-360,360)
    Y = Y-X    
    print "Current angle: " + str(Y)
    print "Applied course: " + str(X)
    time.sleep(1)
    
main()