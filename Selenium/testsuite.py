import unittest

from testcase1 import TestCase1
from testcase2 import TestCase2

class TestSuite(unittest.TestCase):

	def suite():
		suite = unittest.TestSuite()
		suite.addTest(TestCase1("test_waitForCheckoutPhotosButton"))
		suite.addTest(TestCase2("test_AssertTitle"))
		return suite

		
if __name__ == "__main__":
	unittest.main()