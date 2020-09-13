import simpy
import random
from src.logger import t, Action
from src.order import Order


class Courier(simpy.Event):
    def __init__(self, env, order: Order):
        super()
        self.env = env
        self.order = order
        self.time = random.uniform(2, 6)
        print(self)

    def __repr__(self):
        return '{:.0f} [C] {} - {} - RES: '.format(self.env.now, self.order.id[0:5], self.order.name.ljust(20), self.env.coordinator)
