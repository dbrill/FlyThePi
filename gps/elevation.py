import matplotlib.pyplot as plt
import numpy as np
import csv

# Initiate arrays
time = []
alt = []
speed = []

# Read values into arrays
with open("collect.csv", "rb") as f:
	reader = csv.reader(f,delimiter=",")
	for row in reader:
		alt.append(row[3])
		speed.append(row[4])

#Convert to numpy
b = np.array(alt)
c = np.array(speed)

#Delete headers
new_alt = np.delete(alt, 0)
new_speed = np.delete(speed, 0)

# Make Time data for X axis
for i in range(0, len(new_speed)):
	time.append(i * 5)


#Build Plots
plt.figure(1)
plt.subplot(211)
plt.plot(time, new_alt, 'b--')
plt.xlabel('Time (Seconds)')
plt.ylabel('Meters')
plt.title('Elevation')

plt.subplot(212)
plt.plot(time, new_speed, 'ro')
plt.xlabel('Time (Seconds)')
plt.ylabel('Meters/Second')
plt.title('Speed')

plt.subplots_adjust(hspace = 1)
plt.savefig('stats.png')


