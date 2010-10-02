
from unittest import makeSuite, TestCase, TestSuite
import main

class TestMkHex(TestCase):

    def testZero(self):
        self.assertEqual(main.mkHex(0.0),"00")

    def testFull(self):
        self.assertEqual(main.mkHex(1.0) , "ff")

    def testOne(self):
        self.assertEqual(main.mkHex(1.0/255) , "01")

    def testFifteen(self):
        self.assertEqual(main.mkHex(15.0/255) , "0f")

    def test254(self):
        self.assertEqual(main.mkHex(254.0/255) , "fe")

def get_tests():
    TS = TestSuite()
    TS.addTest(makeSuite(TestMkHex))
    return TS
