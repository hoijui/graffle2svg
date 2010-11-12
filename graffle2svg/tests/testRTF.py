
from unittest import makeSuite, TestCase, TestSuite
from rtf import extractRTFString, ColorTable

class TestRTF(TestCase):
    """Tests with valid RTF"""
    def testSimple(self):
        '''assert extractRTFString(r"{\rtf1\ansi testing}")["string"]=="testing"'''
        lines = extractRTFString(r"{\rtf1\ansi testing}")
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]["string"],"testing")

    def testfontweight(self):
        ''' test that font size is correctly applied on spans'''
        lines = extractRTFString(r"{\rtf\ansi\fs10\b testing}")
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0]['style'],  {"font-size":"5.0px","font-weight":"bold"})
        
    def testfont(self):
        lines = extractRTFString(r"""{\rtf1\ansi\ansicpg1252\cocoartf949\cocoasubrtf540
{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red20\green20\blue20;}
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\ql\qnatural\pardirnatural

\f0\fs16 \cf2 \expnd0\expndtw0\kerning0
== LICENSE:\
\
(The MIT License)\
\
Copyright (c) 2007 Tom Preston-\
\
Permission is hereby granted, f\
ree of charge, to any person ob\
}""")
        self.assertEqual(len(lines),8 )


class TestColorTable(TestCase):
    def testsimpleColorTable(self):
        colors = ColorTable()
        colors.parseTable(r'{\colortbl;\red255\green255\blue255;\red75\green75\blue75;}foo', 9)
        self.assertEqual(colors[0], "000000")
        self.assertEqual(colors[1], "ffffff")
        self.assertEqual(colors[2], "4b4b4b")
        
def get_tests():
    import testCascadingStyles
    TS = TestSuite()
    TS.addTest(makeSuite(TestRTF))
    TS.addTest(makeSuite(TestColorTable))
    return TS
