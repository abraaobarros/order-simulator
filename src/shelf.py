import simpy
from logger import t, Action

class SimpleShelf(simpy.FilterStore):
    def __init__(self, env, capacity):
        super().__init__(env,  capacity)
        self.env = env

    def put(self, item):
        super().put(item)

    def __repr__(self):
        if self.isFull():
            return '[FULL] Shelf {} {}'.format(self.items)
        return 'Shelf {} {}'.format(self.items)

    def get_by_order_id(self, order_id):
        order = self.get(lambda order: order.id==order_id)
        return order

    def isFull(self):
        return len(self.items) == self.capacity

class OverflowShelf(SimpleShelf):
    def __init__(self, env, capacity):
        super().__init__(env, capacity)


class ShelvesCoordinator(object):
    def __init__(self, env): 
        super()
        self.env = env
        self.shelves = {}

    def addShelf(self, name, capacity, is_overflow=False):
        if not is_overflow:
            self.shelves[name] = SimpleShelf(env=self.env, capacity=capacity)

    

        