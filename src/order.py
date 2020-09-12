import simpy


class Order(object):
    def __init__(self, json):
        super()
        self.id = json['id']
        self.name = json['name']
        self.temp = json['temp']
        self.shelfLife = json['shelfLife']
        self.decayRate = json['decayRate']
