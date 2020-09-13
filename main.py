
from src.ckitchen import *
from src.helpers import get_initial_orders


def main():
    orders = get_initial_orders()
    core = CKitchen(orders)
    core.simulate()
    core.run(until=100)


if __name__ == '__main__':
    main()
