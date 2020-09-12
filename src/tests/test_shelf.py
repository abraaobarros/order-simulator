import unittest
import sys

from src.ckitchen import *
from src.helpers import get_initial_orders
from src.shelf import *
from src.order import *


class ShelfTestCase(unittest.TestCase):
    def test_should_init_shelf(self):
        core = CKitchen(get_initial_orders())
        shelf = SimpleShelf(core,  capacity=10)
        self.assertIsNotNone(CKitchen, 'should init class')

    def test_should_put_order_until_capacity(self):
        core = CKitchen(get_initial_orders())
        order = Order(get_initial_orders()[0])
        order2 = Order(get_initial_orders()[2])
        shelf = SimpleShelf(core,  capacity=1)
        self.assertIsNotNone(shelf.get())
        shelf.put(order)
        shelf.put(order2)

        self.assertIn(order, shelf.items)
        self.assertNotIn(order2, shelf.items)

    def test_should_remove_filtered_order(self):
        core = CKitchen(get_initial_orders()[0:5])
        shelf = SimpleShelf(core,  capacity=8)
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

    def test_overflow_put_on_coordinator(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        coordinator = ShelvesCoordinator(core, overflow_capacity=10)
        coordinator.addShelf('hot', 1)
        coordinator.put(hot_orders[0])
        self.assertEqual(len(coordinator.shelves['hot']), 1)
        coordinator.put(hot_orders[1])
        self.assertEqual(len(coordinator.overflow), 1)

    def test_overflow_with_many_shelves(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(core, overflow_capacity=10)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        coordinator.put(hot_orders.pop())
        coordinator.put(hot_orders.pop())
        coordinator.put(freeze_orders.pop())
        coordinator.put(freeze_orders.pop())
        self.assertEqual(len(coordinator.overflow), 2)

    def test_overflow_all_stack_rise_error(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(core, overflow_capacity=1)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        coordinator.put(hot_orders.pop())
        coordinator.put(hot_orders.pop())
        coordinator.put(freeze_orders.pop())

        with self.assertRaises(OverflowFullStackError) as context:
            coordinator.put(freeze_orders.pop())

    def test_find_some_order_to_take_from_overflow_to_shelf(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(core, overflow_capacity=3)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)

        coordinator.put(hot_orders.pop())
        coordinator.put(hot_orders.pop())
        self.assertFalse(coordinator.overflow.has_order_temp('frozen'))
        self.assertTrue(coordinator.overflow.has_order_temp('hot'))

    def test_function_to_discart_order_when_overflow(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']

        def discard(self, cordinator: ShelvesCoordinator):
            pass

        coordinator = ShelvesCoordinator(
            core, overflow_capacity=1, overflowFullFunc=discard)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        coordinator.put(hot_orders.pop())
        coordinator.put(hot_orders.pop())
        coordinator.put(freeze_orders.pop())
        coordinator.put(freeze_orders.pop())


if __name__ == "__main__":
    unittest.main()
