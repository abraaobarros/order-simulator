import simpy

from src.logger import t, Action


class Order(simpy.Event):
    def __init__(self, json, env=None):
        super()
        self.id = json['id']
        self.name = json['name']
        self.temp = json['temp']
        self.shelfLife = json['shelfLife']
        self.decayRate = json['decayRate']
        self.env = env

    def dispatch(self):
        print('{:.0f} [O] {}'.format(self.env.now, self))

    def __repr__(self):
        return '{} - {}[{}] - RES: {}'.format(self.id[0:5], self.name.ljust(20), self.temp, self.env.coordinator)

    def __eq__(self, other):
        return self.id == other.id
