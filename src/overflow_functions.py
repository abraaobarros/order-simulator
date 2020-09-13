import random
from src.shelf import *
from src.order import *


def move_available_shelf_full_overflow(coordinator: ShelvesCoordinator, order: Order):
    for temp in coordinator.shelves:
        if not coordinator.shelves[temp].isFull() and coordinator.overflow.has_order_temp(temp):
            item = coordinator.overflow.get_by_temp(temp)
            coordinator.get(item)
            coordinator.shelves[temp].put(item)
            coordinator.overflow.put(order)
            break


def discard_full_overflow(coordinator: ShelvesCoordinator, order: Order):
    print('[D] {} {}'.format(order, coordinator))


def discard_randomly_full_overflow(coordinator: ShelvesCoordinator, order: Order):
    item_to_discard = random.choice(coordinator.overflow.items)
    coordinator.get(item_to_discard)
    coordinator.put(order)
