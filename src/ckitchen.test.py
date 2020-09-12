import unittest
import sys

from ckitchen import *
from helpers import get_initial_orders

class CoreTestCase(unittest.TestCase):
    def test_should_init_core(self):
        core = CKitchen()
        self.assertIsNotNone(CKitchen)

    def test_should_load_orders_on_constructor(self):
        core = CKitchen(get_initial_orders())
        self.assertIsNotNone(core.items)
        self.assertEqual(len(core.items), 132)

    def test_change_parameters_simulation(self):
        core = CKitchen(get_initial_orders())
        self.assertEqual(core.parameters.INTERVAL_ORDERS, CKParameters.INTERVAL_ORDERS)

        parameters = CKParameters
        parameters.INTERVAL_ORDERS = 4
        core = CKitchen(get_initial_orders(), parameters=parameters)
        self.assertEqual(core.parameters.INTERVAL_ORDERS, 4)





if __name__ == "__main__":
    unittest.main()