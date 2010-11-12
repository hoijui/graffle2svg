
from unittest import makeSuite, TestCase, TestSuite
import main
import xml.dom.minidom

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

class TestGraffleParser(TestCase):
    def setUp(self):
        self.gp = main.GraffleParser()
    
    def tearDown(self):
        del self.gp

    def testGraffleDictInteger(self):
        p = xml.dom.minidom.parseString("<dict><key>ImageCounter</key><integer>1</integer></dict>")
        dict = self.gp.ReturnGraffleDict(p.firstChild)
        self.assertEqual(dict['ImageCounter'], '1')
 
    def testGraffleDictReal(self):
        p = xml.dom.minidom.parseString("<dict><key>Size</key><real>19</real></dict>")
        dict = self.gp.ReturnGraffleDict(p.firstChild)
        self.assertEqual(dict['Size'], '19')

    def testGraffleDictReal(self):
        p = xml.dom.minidom.parseString("<dict><key>Shape</key><string>RoundRect</string></dict>")
        dict = self.gp.ReturnGraffleDict(p.firstChild)
        self.assertEqual(dict['Shape'], 'RoundRect')


def get_tests():
    TS = TestSuite()
    TS.addTest(makeSuite(TestMkHex))
    TS.addTest(makeSuite(TestGraffleParser))
    return TS
