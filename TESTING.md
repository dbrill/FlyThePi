**Who:** Danny Brill, Dan Bye, Sarah Godine, Bryan Hawthorne, Lucy Wilkinson

**Title:** FlyThePi

**Vision:** You lose it, we find it.

**Automated Tests** 

Explanation: Used the Python unittest module to handle our automated testing.

Usage: ```python rungps_test.py```
__Make sure__ ```rungps.py``` is in your current working directory.

Output:

```
user@cu-cs-vm:$ python rungps_test.py 

EF..EFFF.
======================================================================
ERROR: test_HeightValue (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 27, in test_HeightValue
    self.assertNotEqual(gpspoll.getHeight(), nan, "GPS isn't returning height")
NameError: global name 'nan' is not defined

======================================================================
ERROR: test_PositionValue (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 39, in test_PositionValue
    self.assertNotEqual(gpspoll.running, (nan, nan), "GPS isn't returning coordinates")
NameError: global name 'nan' is not defined

======================================================================
FAIL: test_LowerHeightLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 31, in test_LowerHeightLimit
    self.assertLess(0, gpspoll.getHeight(), "GPS in Australia")
AssertionError: GPS in Australia

======================================================================
FAIL: test_UpperHeightLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 35, in test_UpperHeightLimit
    self.assertGreater(321869, gpspoll.getHeight(), "GPS in Orbit")
AssertionError: GPS in Orbit

======================================================================
FAIL: test_UpperLatitudeLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 47, in test_UpperLatitudeLimit
    self.assertLess(41, gpspoll.getLatitude(), "GPS is North of CO")
AssertionError: GPS is North of CO

======================================================================
FAIL: test_UpperLongitudeLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 55, in test_UpperLongitudeLimit
    self.assertGreater(-102, gpspoll.getLongitude(), "GPS is East of CO")
AssertionError: GPS is East of CO

----------------------------------------------------------------------
Ran 9 tests in 0.002s

FAILED (failures=4, errors=2)
user@cu-cs-vm:~/Dropbox/SP2016/3308/Group Project$ python rungps_test.py > tests.txt
EF..EFFF.
======================================================================
ERROR: test_HeightValue (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 27, in test_HeightValue
    self.assertNotEqual(gpspoll.getHeight(), nan, "GPS isn't returning height")
NameError: global name 'nan' is not defined

======================================================================
ERROR: test_PositionValue (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 39, in test_PositionValue
    self.assertNotEqual(gpspoll.running, (nan, nan), "GPS isn't returning coordinates")
NameError: global name 'nan' is not defined

======================================================================
FAIL: test_LowerHeightLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 31, in test_LowerHeightLimit
    self.assertLess(0, gpspoll.getHeight(), "GPS in Australia")
AssertionError: GPS in Australia

======================================================================
FAIL: test_UpperHeightLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 35, in test_UpperHeightLimit
    self.assertGreater(321869, gpspoll.getHeight(), "GPS in Orbit")
AssertionError: GPS in Orbit

======================================================================
FAIL: test_UpperLatitudeLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 47, in test_UpperLatitudeLimit
    self.assertLess(41, gpspoll.getLatitude(), "GPS is North of CO")
AssertionError: GPS is North of CO

======================================================================
FAIL: test_UpperLongitudeLimit (__main__.RungpsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "rungps_test.py", line 55, in test_UpperLongitudeLimit
    self.assertGreater(-102, gpspoll.getLongitude(), "GPS is East of CO")
AssertionError: GPS is East of CO

----------------------------------------------------------------------
Ran 9 tests in 0.007s

FAILED (failures=4, errors=2)

```

**User Acceptance Tests**
![alt text] (https://github.com/dbrill/FlyThePi/blob/master/UC-01.png)
![alt text] (https://github.com/dbrill/FlyThePi/blob/master/UC-02.png)
![alt text] (https://github.com/dbrill/FlyThePi/blob/master/UC-03.png)
