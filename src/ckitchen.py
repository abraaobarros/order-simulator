import simpy

from src.order import Order
from src.shelf import ShelvesCoordinator
from src.courier import Courier


class CKParameters(object):
    RANDOM_SEED = 42
    INTERVAL_ORDERS = 0.5
    MIN_COURIER_TIME = 2
    MAX_COURIER_TIME = 6
    OVERFLOW_DECAY_MODIFIER = 2
    NORMAL_DECAY_MODIFIER = 1


class CKitchen(simpy.Environment):

    def __init__(self, orders: [Order] = [], parameters=CKParameters, coordinator=None):
        super().__init__()
        self.orders = list([Order(order, self) for order in orders])
        self.parameters = parameters
        if(coordinator is None):
            self.coordinator = ShelvesCoordinator(self, 15)
            self.coordinator.addShelf('hot', 10)
            self.coordinator.addShelf('frozen', 10)
            self.coordinator.addShelf('cold', 10)
        else:
            self.coordinator = coordinator

    def setCoordinator(self, coordinator):
        self.coordinator = coordinator

    def simulate(self):
        self.process(self.dispatch_orders())

    def dispatch_orders(self):
        for order in self.orders:
            order.dispatch()
            self.coordinator.put(order)
            self.process(self.dispatch_courier(order))
            yield self.timeout(self.parameters.INTERVAL_ORDERS)

    def dispatch_courier(self, order):
        courier = Courier(self, order)
        yield self.timeout(courier.time)
        self.coordinator.get(order)
        if(order.value() > 0):
            courier.deliver(order)
        else:
            courier.discard(order)

    def __repr__(self):
        return " {} {} ".format(self.orders, self.coordinator)
