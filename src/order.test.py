import unittest
import sys

from order import *
from helpers import get_initial_orders

class OrderTestCase(unittest.TestCase):
    def test_should_init_order(self):
        order = Order()
        self.assertIsNotNone(order)

    def test_should_init_order(self):
        orders_list = get_initial_orders()
        order = Order(orders_list[0])
        self.assertEqual(order.id, orders_list[0]['id'])
        self.assertEqual(order.name, orders_list[0]['name'])
        self.assertEqual(order.temp, orders_list[0]['temp'])
        self.assertEqual(order.shelfLife, orders_list[0]['shelfLife'])
        self.assertEqual(order.decayRate, orders_list[0]['decayRate'])

    
        


if __name__ == "__main__":
    unittest.main()