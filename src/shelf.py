import simpy
from src.logger import t, Action


class SimpleShelf(simpy.FilterStore):
    def __init__(self, env, capacity):
        super().__init__(env,  capacity)
        self.env = env

    def put(self, item):
        super().put(item)

    def __repr__(self):
        if self.isFull():
            return '[FULL] Shelf {}'.format(self.items)
        return 'Shelf {}'.format(self.items)

    def get_by_order_id(self, order_id):
        order = self.get(lambda order: order.id == order_id)
        return order

    def get_by_temp(self, temp):
        order = self.get(lambda order: order.temp == temp)
        return order

    def has_order_temp(self, temp):
        for item in self.items:
            if(item.temp == temp):
                return True
        return False

    def isFull(self):
        return len(self.items) == self.capacity

    def __len__(self):
        return len(self.items)


class OverflowShelf(SimpleShelf):
    def __init__(self, env, capacity):
        super().__init__(env, capacity)


class ShelvesCoordinator(simpy.Event):
    def __init__(self, env, overflow_capacity=10, overflowFullFunc=None):
        super()
        self.env = env
        self.shelves = {}
        self.overflow = OverflowShelf(env, overflow_capacity)
        self.overflowFullFunc = overflowFullFunc

    def addShelf(self, name, capacity):
        self.shelves[name] = SimpleShelf(env=self.env, capacity=capacity)

    def put(self, order):
        pass
        if(self.shelves[order.temp].isFull()):
            if(self.overflow.isFull()):
                if self.overflowFullFunc is not None:
                    self.overflowFullFunc(self, order)
                else:
                    pass
            self.overflow.put(order)
        else:
            self.shelves[order.temp].put(order)

    def where_is(self, order):
        if(order in self.shelves[order.temp].items):
            return order.temp
        elif(order in self.overflow.items):
            return 'overflow'
        else:
            return 'missing'

    def get(self, order):
        shelf_name = self.where_is(order)
        if(shelf_name == 'missing'):
            print('{:.0f} [D] {}[missing]'.format(self.env.now, order))
            return None
        elif(shelf_name == 'overflow'):
            print('{:.0f} [D] {}[overflow]'.format(self.env.now, order))
            return self.overflow.get_by_order_id(order.id)
        else:
            print('{:.0f} [D] {}[{}]'.format(self.env.now, order, order.temp))
            return self.shelves[shelf_name].get_by_order_id(order.id)

    def __repr__(self):
        text = "[S]:"
        for key in self.shelves:
            text += "[{}] {} ".format(key, len(self.shelves[key]))
        text += '[{}]:{}'.format('overflow', len(self.overflow))
        return text


class OverflowFullStackError(Exception):
    def __init__(self):
        super().__init__('The Overflow Stack is full')
