import unittest

from src.helpers import get_initial_orders
from src.order import Order


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

    def test_calculate_initial_value_after_dispatched(self):
        pass


if __name__ == "__main__":
    unittest.main()
