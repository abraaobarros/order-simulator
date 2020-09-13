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


def cli():
    argv = sys.argv
    orders = get_initial_orders()
    parameters = CKParameters()
    if argv.index('--interval_orders') != -1:
        parameters.INTERVAL_ORDERS = float(
            argv[argv.index('--interval_orders')+1])

    if argv.index('--max_courier_time') != -1:
        parameters.MAX_COURIER_TIME = float(
            argv[argv.index('--max_courier_time')+1])

    if argv.index('--min_courier_time') != -1:
        parameters.MIN_COURIER_TIME = float(
            argv[argv.index('--min_courier_time')+1])

    if argv.index('--overflow_decay_modifier') != -1:
        parameters.OVERFLOW_DECAY_MODIFIER = float(
            argv[argv.index('--overflow_decay_modifier')+1])

    if argv.index('--normal_decay') != -1:
        parameters.NORMAL_DECAY_MODIFIER = float(
            argv[argv.index('--normal_decay')+1])

    core = CKitchen(orders, parameters=parameters)
    core.simulate()
    core.run()


if __name__ == '__main__':
    main()
