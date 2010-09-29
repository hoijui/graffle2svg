"""test collector"""

from unittest import makeSuite, TestCase, TestSuite

class TestMe(TestCase):
    def test_ok(self):
        pass

def get_tests():
    import testCascadingStyles, testRTF, testGeom, testMain
    TS = TestSuite()
    TS.addTest(testCascadingStyles.get_tests())
    TS.addTest(testRTF.get_tests())
    TS.addTest(testGeom.get_tests())
    TS.addTest(testMain.get_tests())
    return TS
