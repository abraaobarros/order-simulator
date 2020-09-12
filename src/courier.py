import simpy
from logger import t, Action
from order import Order

class Courier(simpy.Event):
    def __init__(self, order:Order):
        super()
        self.order = order

    def dispatch(self, env):
        t(self, Action.START, env)
        t(self, Action.END, env)


    def __repr__(self):
        return 'Corrier {} - {}'.format(self.order.id, self.order.name)

