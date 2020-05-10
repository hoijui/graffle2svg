"""test collector"""

from unittest import TestSuite
import tests.testCascadingStyles
import tests.testRTF
import tests.testGeom
import tests.testMain

def get_tests():
    test_suite = TestSuite()
    test_suite.addTest(testCascadingStyles.get_tests())
    test_suite.addTest(testRTF.get_tests())
    test_suite.addTest(testGeom.get_tests())
    test_suite.addTest(testMain.get_tests())
    return test_suite
