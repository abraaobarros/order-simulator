
from src.ckitchen import *
from src.helpers import get_initial_orders


def main():
    orders = get_initial_orders()
    parameters = CKParameters()
    parameters.INTERVAL_ORDERS = 0.2
    parameters.MAX_COURIER_TIME = 20
    parameters.MIN_COURIER_TIME = 19
    core = CKitchen(orders, parameters=parameters)
    core.simulate()
    core.run(until=100)


if __name__ == '__main__':
    main()
