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
        self.assertNotEqual(gpspoll.getHeight(), Nan, "GPS isn't returning height")

    def test_getHeight(self):
        gpspoll = rungps.GpsPoll()
        self.assert

