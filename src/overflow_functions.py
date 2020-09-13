import random
from src.order import *


def move_available_shelf_full_overflow(coordinator, order: Order):
    for temp in coordinator.shelves:
        if not coordinator.shelves[temp].isFull() and coordinator.overflow.has_order_temp(temp):
            item = coordinator.overflow.get_by_temp(temp)
            coordinator.get(item)
            item.setShelfDecayModifier(
                coordinator.env.parameters.NORMAL_DECAY_MODIFIER)
            coordinator.shelves[temp].put(item)
            coordinator.overflow.put(order)
            return True
    return False


def discard_full_overflow(coordinator, order: Order):
    print('[  discarded  ] {} {}'.format(order, coordinator))


def discard_randomly_full_overflow(coordinator, order: Order):
    item_to_discard = random.choice(coordinator.overflow.items)
    coordinator.get(item_to_discard)
    coordinator.put(order)


def move_and_discard_ramdomly_full_overflow(coordinator, order: Order):
    res = move_available_shelf_full_overflow(coordinator, order)
    if(not res):
        discard_randomly_full_overflow(coordinator, order)
        print('{:2.2f} [  discard  ] {}'.format(coordinator.env.now, order))
    else:
        print('{:2.2f} [    moved    ] {}'.format(coordinator.env.now, order))
