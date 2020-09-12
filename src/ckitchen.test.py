import unittest
import sys

from ckitchen import *
from helpers import get_initial_orders

class CoreTestCase(unittest.TestCase):
    def test_should_init_core(self):
        core = CKitchen()
        self.assertIsNotNone(CKitchen, 'should init class')

    def test_should_load_orders_on_constructor(self):
        core = CKitchen(get_initial_orders())
        self.assertIsNotNone(core.orders)
        self.assertEqual(len(core.orders), 132, 'number of order is not the same of source')

    def test_change_parameters_simulation(self):
        core = CKitchen(get_initial_orders())
        self.assertEqual(core.parameters.INTERVAL_ORDERS, CKParameters.INTERVAL_ORDERS)
        parameters = CKParameters
        parameters.INTERVAL_ORDERS = 4
        core = CKitchen(get_initial_orders(), parameters=parameters)
        self.assertEqual(core.parameters.INTERVAL_ORDERS, 4, 'parameter set is not working propertly')

    def test_initial_order_dispatch(self):
        small_subSet = get_initial_orders()[0:2]
        parameters = CKParameters
        parameters.INTERVAL_ORDERS = 0.5
        core = CKitchen(small_subSet, parameters=CKParameters)
        core.simulate()
        core.run()
        self.assertEqual(core._now, 1, 'should dispatch only 2 orders per second') 




if __name__ == "__main__":
    unittest.main()