#!/usr/bin/env python
from tests import get_tests
import unittest

if __name__ == "__main__":
    suite = get_tests
    unittest.main(defaultTest="suite")
