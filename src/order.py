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

    def dispatch(self):
        print(self)

    def __repr__(self):
        return '[O] {} - {}[{}]'.format(self.id[0:5], self.name, self.temp)

    def __eq__(self, other):
        return self.id == other.id
