import unittest

from src.helpers import get_initial_orders
from src.order import Order
from src.ckitchen import CKitchen
from src.shelf import *
from src.overflow_functions import *


class OverflowFunctionsTestCase(unittest.TestCase):

    def test_should_discard_item_from_coordinator(self):
        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(
            core, overflow_capacity=1, overflowFullFunc=discard_full_overflow)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        order = hot_orders.pop()
        order_to_stay = freeze_orders.pop()
        order_to_move = freeze_orders.pop()
        order_full_overflow = hot_orders.pop()

        coordinator.put(order)
        coordinator.put(order_to_stay)
        coordinator.put(order_to_move)

        coordinator.get(order_to_stay)
        coordinator.put(order_full_overflow)
        self.assertEqual(coordinator.where_is(order_full_overflow), 'missing')

    def test_should_move_item_to_empty_shelve_from_coordinator(self):

        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(
            core, overflow_capacity=1, overflowFullFunc=move_available_shelf_full_overflow)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        order = hot_orders.pop()
        order_to_stay = freeze_orders.pop()
        order_to_move = freeze_orders.pop()
        order_full_overflow = hot_orders.pop()

        coordinator.put(order)
        coordinator.put(order_to_stay)
        coordinator.put(order_to_move)

        coordinator.get(order_to_stay)
        coordinator.put(order_full_overflow)
        self.assertEqual(coordinator.where_is(order_full_overflow), 'overflow')
        self.assertEqual(coordinator.where_is(order_to_move), 'frozen')

    def test_should_discard_random_item(self):

        core = CKitchen(get_initial_orders())
        hot_orders = [o for o in core.orders if o.temp == 'hot']
        freeze_orders = [o for o in core.orders if o.temp == 'frozen']
        coordinator = ShelvesCoordinator(
            core, overflow_capacity=1, overflowFullFunc=discard_randomly_full_overflow)
        coordinator.addShelf('hot', 1)
        coordinator.addShelf('frozen', 1)
        order = hot_orders.pop()
        order_to_stay = freeze_orders.pop()
        order_to_move = freeze_orders.pop()
        order_full_overflow = hot_orders.pop()

        coordinator.put(order)
        coordinator.put(order_to_stay)
        coordinator.put(order_to_move)

        coordinator.get(order_to_stay)
        coordinator.put(order_full_overflow)
        self.assertEqual(coordinator.where_is(order_full_overflow), 'overflow')
        self.assertEqual(coordinator.where_is(order_to_move), 'missing')


if __name__ == "__main__":
    unittest.main()
