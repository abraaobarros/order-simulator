import simpy

from src.logger import t, Action


class Order(simpy.Event):
    def __init__(self, json):
        super()
        self.id = json['id']
        self.name = json['name']
        self.temp = json['temp']
        self.shelfLife = json['shelfLife']
        self.decayRate = json['decayRate']

    def dispatch(self, env):
        t(self, Action.START, env)
        t(self, Action.END, env)

    def __repr__(self):
        return 'Order {}'.format(self.id)

    def __eq__(self, other):
        return self.id == other.id
