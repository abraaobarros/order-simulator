import unittest
import sys

from ckitchen import CKitchen

class CoreTestCase(unittest.TestCase):
    def test_should_init_core(self):
        core = CKitchen()
        self.assertIsNotNone(CKitchen)


if __name__ == "__main__":
    unittest.main()