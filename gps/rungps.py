#! /usr/bin/python
 
import os
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
    while gpsp.running:
      gpsd.next() #Gets the next set of data and clears the buffer
 
if __name__ == '__main__':
  gpspoll = GpsPoll() # Thread creation
  try:
    gpsp.start() 
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
'''      print 'Eps         ' , gpsd.fix.eps
      print 'Epx         ' , gpsd.fix.epx
      print 'Epv         ' , gpsd.fix.epv
      print 'Ept         ' , gpsd.fix.ept '''
      print 'Speed (m/s) ' , gpsd.fix.speed
      print 'Climb       ' , gpsd.fix.climb
      print 'Track       ' , gpsd.fix.track
      print 'Mode        ' , gpsd.fix.mode
      print
      print 'Satellites:        ' , gpsd.satellites
 
      time.sleep(5) #Refresh rate
 
  except (KeyboardInterrupt, SystemExit): # Control-C functionality
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # Wait for the thread to finish.
  print "Exiting..."
