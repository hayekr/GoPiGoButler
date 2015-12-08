#GOPIGO API http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

#imports
from gopigo import *
import time

__author__ = 'Robert Hayek'

servo(80)

class Pigo:
    sweep = [None] * 160  #the list to hold scanning data
    MIN_DIST = 50  #distance used when plotting a clear direction... longer so we're planning farther ahead
    status = {'isMoving' : False, 'servo': 90, 'leftSpeed' : 175, 'rightSpeed' : 175, "distance" : 100}
    def __init__(self):
        print "NOW RUNNING OBSTACLE AVOIDER"

    def servoSweep(self):
        for angle in range(15, 150, 5):
            servo(angle)
            time.sleep(.10)
            self.sweep['angle'] = us_dist(15)
            print self.sweep[angle]

    def checkDistance(self):
        self.status['distance'] = us_dist(15)
        print "CHECKING DISTANCE..." + "SOMETHING IS " + str(self.status['distance']) + "mm away"

    def findaPath(self):
        for angle in self.sweep:
            counter = 0
            if self.sweep[angle] > MIN_DIST:
                counter += 1
            else:
                counter = 0
            if counter == 20:
                return True
        return False


butler = Pigo()

''' while  True:
    if butler.servoScan():
        butler.safeDrive()
    if butler.findaPath():
        butler.turnTo(butler.findAngle())
    else:
        butler.turnAround()
butler.stop()
'''
butler.servoSweep()
print butler.findaPath()


