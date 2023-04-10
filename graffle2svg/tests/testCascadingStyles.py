#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2009 Tim Wintle
# SPDX-FileCopyrightText: 2010 - 2020 Jean-Noël Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2015 Stéphane Galland <galland@arakhne.org>
# SPDX-FileCopyrightText: 2023 Robin Vobruba <hoijui.quaero@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

from unittest import makeSuite, TestCase, TestSuite

from styles import CascadingStyles

class TestDefaults(TestCase):
    def setUp(self):
        self.cs = CascadingStyles({"font":"arial","font-size":"12pt"})

    def testNone(self):
        self.assertEqual(str(self.cs), "")

    def testRemoveScope(self):
        self.cs.appendScope()
        self.cs["font"] = "newfont"
        self.cs.popScope()
        self.assertEqual(str(self.cs), "")


    def testIgnoreDefault(self):
        self.cs.appendScope()
        self.cs["font"] = "newfont"
        self.cs.appendScope()
        self.cs["font"] = "arial"
        self.assertEqual(str(self.cs), "")


class TestScope(TestCase):
    def setUp(self):
        self.cs = CascadingStyles({"font":"arial","font-size":"12pt"})

    def testRemoveScope(self):
        self.cs.appendScope()
        self.cs["font"] = "newfont"
        self.cs["font"] == "newfont"

def get_tests():
    TS = TestSuite()
    TS.addTest(makeSuite(TestDefaults))
    TS.addTest(makeSuite(TestScope))
    return TS
