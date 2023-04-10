# SPDX-FileCopyrightText: 2009 Tim Wintle
# SPDX-FileCopyrightText: 2010 - 2020 Jean-Noël Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2010 Jean-Noel Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2015 Stéphane Galland <galland@arakhne.org>
#
# SPDX-License-Identifier: BSD-3-Clause

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
