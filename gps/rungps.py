#! /usr/bin/python

import os
import csv
from gps import *
from time import *
import time
import threading

gpsd = None

os.system('clear') #clears the terminal for nicer output

# Class for creating gps threads
class GpsPoll(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE) #start gps data stream
        self.current_value = None
        self.running = True

    def run(self):
        global gpsd
        while gpspoll.running:
          gpsd.next() #Gets the next set of data and clears the buffer

    def getHeight(self):
        return gpsd.fix.altitude
        
    def getLatitude(self):
        return gpsd.fix.latitude

    def getLongitude(self):
        return gpsd.fix.longitude

    def getPosition(self):
        return (gpsd.fix.latitude, gpsd.fix.longitude)

    def getSpeed(self):
        return gpsd.fix.speed

    def getClimb(self):
        return gpsd.fix.climb

    def getTrack(self):
        return gpsd.fix.track

if __name__ == '__main__':
    gpspoll = GpsPoll() # Thread creation
    try:
        gpspoll.start()
	csvdata = csv.writer(open("collect_test.csv", "wb"))
	csvdata.writerow(["Latitude", "Longitude", "UTC Time", "Elevation", "Speed", "Heading"])
        while True:
            # Wait a few seconds to get accurate data

            os.system('clear')

            print
            print ' GPS reading'
            print '----------------------------------------'
            print 'Latitude:    ' , gpsd.fix.latitude
            print 'Longitude:   ' , gpsd.fix.longitude
            print 'Time UTC:    ' , gpsd.utc,' + ', gpsd.fix.time
            print 'Altitude (m)' , gpsd.fix.altitude
            print 'Speed (m/s) ' , gpsd.fix.speed
            print 'Climb       ' , gpsd.fix.climb
            print 'Track       ' , gpsd.fix.track
            print 'Mode        ' , gpsd.fix.mode
            print
            print 'Satellites:        ' , gpsd.satellites
	    
	    csvdata.writerow([gpsd.fix.latitude, gpsd.fix.longitude, gpsd.utc, gpsd.fix.altitude, gpsd.fix.speed, gpsd.fix.track])

            time.sleep(5) #Refresh rate

    except (KeyboardInterrupt, SystemExit): # Control-C functionality
        print "\nKilling Thread..."
        gpspoll.running = False
        gpspoll.join() # Wait for the thread to finish.
        print "Exiting..."
