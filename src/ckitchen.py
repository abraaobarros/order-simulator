import simpy
from enum import Enum
from order import Order
from shelf import SimpleShelf, OverflowShelf, ShelvesCoordinator


class CKParameters(object):
    RANDOM_SEED = 42
    INTERVAL_ORDERS = 0.5
    MIN_COURIER_TIME = 2
    MAX_COURIER_TIME = 6


class CKitchen(simpy.Environment):

    def __init__(self, orders: [Order] = [], parameters=CKParameters):
        super().__init__()
        self.orders = list([Order(order) for order in orders])
        self.parameters = parameters
        self.coordinator = ShelvesCoordinator(self, 15)
        self.coordinator.addShelf('hot', 10)
        self.coordinator.addShelf('frozen', 10)
        self.coordinator.addShelf('cold', 10)

    def simulate(self):
        self.process(self.dispatch_orders())

    def dispatch_orders(self):
        for order in self.orders:
            order.dispatch(self)
            req = self.coordinator.put(order)
            yield self.timeout(self.parameters.INTERVAL_ORDERS)

    def __repr__(self):
        return " {} {} ".format(self.orders, self.coordinator)
