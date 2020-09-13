import simpy
import random
from src.order import Order
from src.shelf import ShelvesCoordinator
from src.courier import Courier


class CKParameters(object):
    """  Parameters to customize the simulation 
        _RANDOM_SEED_ - seed to reproduce the data given by a pseudo-random and get the same result
        _INTERVAL_ORDERS_ = Interval between orders. ex. 0.5 = 2orders/s
        _MIN_COURIER_TIME_ = Minimum time to courier arrive to get the order on pickup area
        _MAX_COURIER_TIME_ = Max time to courier arrive to get the order on pickup area
        _OVERFLOW_DECAY_MODIFIER_ = Modifier that multiplies order value formula to decay faster when they are in overflow shelf.
    """
    RANDOM_SEED = 42
    INTERVAL_ORDERS = 0.5
    MIN_COURIER_TIME = 2
    MAX_COURIER_TIME = 6
    OVERFLOW_DECAY_MODIFIER = 2
    NORMAL_DECAY_MODIFIER = 1


class CKitchen(simpy.rt.RealtimeEnvironment):
    """
        _factor_ - It is the simulator velocity

        Possible events: 
        _[received]_ - delivery order enter on sistem
        _[picked]_ - courier take out order item on a shelf
        _[wasted]_ - order item can not be delivered because its value is less than zero
        _[not found]_ - courier release order process because the item is not on any shelve
        _[moved]_ - if the overflow shelf is full, this action happens when is possible to move some item to the right temp shelf and put the upcoming order on overflow
        _[gone]_ - when the courier look if his order was on the pickup area and it was not there
        _[discarded]_ - when the movement between shelves is not possible, a random item from overflow is discarded
        _[delivered]_ - when the courier delivers the order.
    """

    def __init__(self, orders=[], parameters=CKParameters, coordinator=None, factor=1):
        super().__init__(factor=factor)
        random.seed(parameters.RANDOM_SEED)
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
            self.coordinator.put(order)
            order.dispatch()
            self.process(self.dispatch_courier(order))
            yield self.timeout(self.parameters.INTERVAL_ORDERS)

    def dispatch_courier(self, order):
        courier = Courier(self, order)
        yield self.timeout(courier.time)
        item = self.coordinator.get(order)
        if item is not None:
            if(order.value() > 0):
                courier.deliver(order)
            else:
                courier.discard(order)
        else:
            courier.missing(order)
