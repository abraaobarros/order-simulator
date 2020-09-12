import json

from pathlib import Path
def get_initial_orders():
    with open('./src/resources/orders.json') as f:
        orders = json.load(f)
    return orders
