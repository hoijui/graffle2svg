#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2009 Tim Wintle
# SPDX-FileCopyrightText: 2010 - 2012 Jean-Noel Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2015 Stéphane Galland <galland@arakhne.org>
# SPDX-FileCopyrightText: 2020 Jean-Noël Avila <jn.avila@free.fr>
# SPDX-FileCopyrightText: 2023 Robin Vobruba <hoijui.quaero@gmail.com>
#
# SPDX-License-Identifier: BSD-3-Clause

import unittest

from tests import get_tests

if __name__ == "__main__":
	suite = get_tests
	unittest.main(defaultTest="suite")
