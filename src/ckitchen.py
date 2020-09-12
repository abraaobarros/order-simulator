import simpy
from enum import Enum

class CKParameters(object):
    RANDOM_SEED = 42
    INTERVAL_ORDERS = 0.1
    MIN_COURIER_TIME = 2
    MAX_COURIER_TIME = 6

class CKitchen(simpy.Environment):
    
    def __init__(self, orders = [], parameters = CKParameters):
        super()
        self.items = orders
        self.parameters = parameters

    