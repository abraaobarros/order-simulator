import simpy
import random
from src.logger import t, Action
from src.order import Order


class Courier(simpy.Event):
    def __init__(self, env, order: Order):
        super().__init__(env)
        self.env = env
        self.order = order
        self.time = random.uniform(2, 6)
        print(self)

    def dispatch(self, env):
        pass

    def __repr__(self):
        return 'Corrier {} - {}'.format(self.order.id, self.order.name)
