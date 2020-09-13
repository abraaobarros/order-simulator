import unittest

from src.helpers import get_initial_orders
from src.courier import Courier
from src.ckitchen import CKitchen
import src.order import Order


class CourierTestCase(unittest.TestCase):
    def test_should_init_courier(self):
        orders = get_initial_orders()
        core = CKitchen(orders=orders)
        courier = Courier(core, core.orders[0])
        self.assertIsNotNone(courier)


if __name__ == "__main__":
    unittest.main()
