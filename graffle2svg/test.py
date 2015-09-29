#!/usr/bin/env python

import unittest

from graffle2svg.tests import get_tests

if __name__ == "__main__":
	suite = get_tests
	unittest.main(defaultTest="suite")
