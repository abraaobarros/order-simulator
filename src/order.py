import simpy


class Order(simpy.Event):
    def __init__(self, json, env=None):
        super()
        self.id = json['id']
        self.name = json['name']
        self.temp = json['temp']
        self.shelfLife = json['shelfLife']
        self.decayRate = json['decayRate']
        self.start = -1
        self.shelfDecayModifier = 1
        self.env = env

    def dispatch(self):
        self.start = self.env.now
        print('{:2.2f} [    order    ] {}'.format(self.env.now, self))

    def __repr__(self):
        return '{} - {}{}({:.3f})*({}) - RES: {}'.format(self.id[0:5],  self.name.ljust(25), self.temp.ljust(9), self.value(), self.shelfDecayModifier, self.env.coordinator)

    def value(self):
        return (self.shelfLife - self.decayRate * self.orderAge() * self.shelfDecayModifier)/self.shelfLife

    def orderAge(self):
        return self.env.now - self.start

    def setShelfDecayModifier(self, value):
        self.shelfDecayModifier = value

    def __eq__(self, other):
        return self.id == other.id
