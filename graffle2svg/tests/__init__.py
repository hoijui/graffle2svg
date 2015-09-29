"""test collector"""

from unittest import makeSuite, TestCase, TestSuite

def get_tests():
	from graffle2svg.tests import testCascadingStyles
	from graffle2svg.tests import testRTF
	from graffle2svg.tests import testGeom
	from graffle2svg.tests import testMain
	TS = TestSuite()
	TS.addTest(testCascadingStyles.get_tests())
	TS.addTest(testRTF.get_tests())
	TS.addTest(testGeom.get_tests())
	TS.addTest(testMain.get_tests())
	return TS
