import json


def get_initial_orders():
    with open('../../resources/orders.json') as f:
        orders = json.load(f)
    return orders
