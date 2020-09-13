
from src.ckitchen import *
from src.helpers import get_initial_orders


def main():
    orders = get_initial_orders()
    parameters = CKParameters()
    parameters.INTERVAL_ORDERS = 0.5
    parameters.MAX_COURIER_TIME = 22
    parameters.MIN_COURIER_TIME = 28
    parameters.OVERFLOW_DECAY_MODIFIER = 10
    parameters.NORMAL_DECAY_MODIFIER = 5
    core = CKitchen(orders, parameters=parameters)
    core.simulate()
    core.run()


if __name__ == '__main__':
    main()
