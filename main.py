from src.ckitchen import *
from src.helpers import get_initial_orders
import sys
import getopt


def main():
    orders = get_initial_orders()
    parameters = CKParameters()
    parameters.INTERVAL_ORDERS = 0.5
    parameters.MAX_COURIER_TIME = 2
    parameters.MIN_COURIER_TIME = 6
    parameters.OVERFLOW_DECAY_MODIFIER = 2
    parameters.NORMAL_DECAY_MODIFIER = 1
    core = CKitchen(orders, parameters=parameters, factor=1)
    core.simulate()
    core.run()


if __name__ == '__main__':
    main()
