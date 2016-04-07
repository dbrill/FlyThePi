import unittest
import rungps

class RungpsTestCase(unittest.TestCase):

    '''    @classmethod
        def setUpClass(cls):
            pass

        @classmethod
        def tearDownClass(cls):
            pass

        def setUp(self):
            pass

        def tearDown(self):
            pass
    '''
    def test_init(self):
    	text = "testing for null values"
    	gpspoll = rungps.GpsPoll()
        self.assertEqual(gpspoll.running, True, "GPS isn't running!")

    def test_HeightValue(self):
        gpspoll = rungps.GpsPoll()
        self.assertNotEqual(gpspoll.getHeight(), nan, "GPS isn't returning height")

    def test_LowerHeightLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertLess(0, gpspoll.getHeight(), "GPS in Australia")

    def test_UpperHeightLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertGreater(321869, gpspoll.getHeight(), "GPS in Orbit")

    def test_PositionValue(self):
        gpspoll = rungps.GpsPoll()
        self.assertNotEqual(gpspoll.running, (nan, nan), "GPS isn't returning coordinates")

    def test_LowerLatitudeLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertGreater(37, gpspoll.getLatitude(), "GPS is South of CO")

    def test_UpperLatitudeLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertLess(41, gpspoll.getLatitude(), "GPS is North of CO")

    def test_LowerLongitudeLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertLess(-109, gpspoll.getLongitude(), "GPS is West of CO")

    def test_UpperLongitudeLimit(self):
        gpspoll = rungps.GpsPoll()
        self.assertGreater(-102, gpspoll.getLongitude(), "GPS is East of CO")



