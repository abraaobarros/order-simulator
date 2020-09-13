import simpy
import random
from src.order import Order
from src.ckitchen import *


class Courier(simpy.Event):
    def __init__(self, env, order: Order):
        super()
        self.env = env
        self.order = order
        self.time = random.uniform(
            env.parameters.MIN_COURIER_TIME, env.parameters.MAX_COURIER_TIME)

    def deliver(self, order):
        print('{:2.2f} [  delivered  ] {}'.format(self.env.now, order))

    def discard(self, order):
        print('{:2.2f} [   wasted    ] {}'.format(self.env.now, order))

    def missing(self, order):
        print('{:2.2f} [  not found  ] {}'.format(self.env.now, order))

    def __repr__(self):
        return '{:.0f} [C] {} - {} - RES: '.format(self.env.now, self.order.id[0:5], self.order.name.ljust(20), self.env.coordinator)
