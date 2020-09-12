import unittest
import sys

sys.path.insert(0, '/root/cloudkitchen/lib')
from ckitchen import CKitchen

class CoreTestCase(unittest.TestCase):
    def test_should_init_core(self):
        core = CKitchen()
        self.assertIsNotNone(CKitchen)


if __name__ == "__main__":
    unittest.main()