import unittest
import rungps

class RungpsTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

	def test_init(self):
		text = "testing for null values"
		gpspoll = rungps.GpsPoll()
        self.assertEqual(gpspoll.running, True, "GPS isn't running!")

    def test_Height(self):
        gpspoll = rungps.GpsPoll()
        self.assertNotEqual(gpspoll.getHeight(), NaN, "GPS isn't returning height")

    def test_getHeight(self):
        gpspoll = rungps.GpsPoll()
        self.assertGreater(gpspoll.getHeight, 0, "you're underground!")

    def test_Speed(self):
        gpspoll = rungps.GpsPoll()
        self.assertNotEqual(gpspoll.getSpeed(), NaN, "GPS isn't returning speed")

    def test_getSpeed(self):
        gpspoll = rungps.GpsPoll()
        self.assertGreater(gpspoll.getSpeed(), 0, "Speed shouldn't be negative, given there's not relative starting point")

    

