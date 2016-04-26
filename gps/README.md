### GPS Code

Preparation:
 - Install [GPSD](http://www.catb.org/gpsd/)
 - Plug in GPS
 - Run ```./gps_reset.sh```

Usage:
 - ```python rungps.py```
 - Must use Ctrl-C to close thread and write to collection CSV file.
 - **Will not write data without GPS Module connected**
 
Visualization:
 - ```python basemap.py``` to generate a map from collect.csv
  - Arrows are pointed in the direction of travel determined by the "Heading" column of ```collect.csv```
  - Arrows are colored by speed determined by "Speed" column of ```collect.csv```
 - ```python elevation.py``` to generate elevation and speed graphs from ```collect.csv```
 
Testing:
  - ```python rungps_test.py```
  - **Tests will not pass unless gps data is being gathered**
