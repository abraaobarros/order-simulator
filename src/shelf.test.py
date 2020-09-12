import unittest
import sys

from ckitchen import *
from helpers import get_initial_orders
from shelf import *
from order import *

class ShelfTestCase(unittest.TestCase):
    def test_should_init_shelf(self):
        core = CKitchen(get_initial_orders())
        shelf = SimpleShelf(core,  capacity=10)
        self.assertIsNotNone(CKitchen, 'should init class')

    def test_should_put_order_until_capacity(self):
        core = CKitchen(get_initial_orders())
        order = Order(get_initial_orders()[0])
        order2 = Order(get_initial_orders()[2])
        shelf = SimpleShelf( core,  capacity=1)
        self.assertIsNotNone(shelf.get())
        shelf.put(order)
        shelf.put(order2)

        self.assertIn(order, shelf.items)
        self.assertNotIn(order2, shelf.items)


    def test_should_remove_filtered_order(self):
        core = CKitchen(get_initial_orders()[0:5])
        shelf = SimpleShelf( core,  capacity=8)
        order_to_filter = core.orders[3]
        for order in core.orders:
            shelf.put(order)
        self.assertIn(order_to_filter, shelf.items)
        order = shelf.get_by_order_id(order_to_filter.id)
        self.assertNotIn(order_to_filter, shelf.items)

    def test_shelves_coordinator_init(self):
        core = CKitchen(get_initial_orders()[0:5])
        coordinator = ShelvesCoordinator(core)
        coordinator.addShelf('hot', 10)
        self.assertIsNotNone(coordinator.shelves['hot'])




if __name__ == "__main__":
    unittest.main()