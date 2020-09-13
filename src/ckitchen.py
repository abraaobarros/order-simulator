import simpy

from src.order import Order
from src.shelf import ShelvesCoordinator
from src.courier import Courier


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
        self.process(self.monitoring_shelves())

    def monitoring_shelves(self):
        while True:
            yield self.timeout(1)
            print(self.now, self.coordinator)

    def dispatch_orders(self):
        for order in self.orders:
            order.dispatch()
            self.coordinator.put(order)
            self.process(self.dispatch_courier(order))
            yield self.timeout(self.parameters.INTERVAL_ORDERS)

    def all_of(self):
        print(self.coordinator)

    def dispatch_courier(self, order):
        courier = Courier(self, order)
        yield self.timeout(courier.time)
        self.coordinator.get(order)

    def __repr__(self):
        return " {} {} ".format(self.orders, self.coordinator)
