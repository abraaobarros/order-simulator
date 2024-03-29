# Engineering Challenge Homework

For the Discrete-Event Simulation of a centralized delivery kitchen, I chose python with simpy to simulate the environment and run the real-time simulation. I found on simpy a simple use of generator function to solve the resources concurrence problem. I used Resource, Event, and Environment from simpy as our model's foundation.

The simpy documentation can be found here: https://simpy.readthedocs.io/en/latest/

## Installation:

### Quickstart:

Run it inside the folder project. Make sure you are using python 3.6+ and pip 19+


```python
pip install -r requirements.txt

```
*If you don't have pip or python installed, follow these instructions: [https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3]

Run it from terminal:

```python

python main.py

```

So, this should be enough to run the project and start the simulation:

![First run](./src/resources/first_run.png)

Each line has the same format:
| tick | event | order_id | order_name | order_temp | order_value | decayFactor | Resources |
|-------|---------|----------|------------|--------|-------|-------------|----------------------------------|
| float | [received] [picked] [wasted] [not found] [moved] [moved] [gone] [discarded] [delivered] | hash | string | string | float | int | [hot] [frozen] [cold] [overflow] |

### Events descriptions:

_[received]_ - delivery order enter on sistem

_[picked]_ - courier take out order item on a shelf

_[wasted]_ - order item can not be delivered because its value is less than zero

_[not found]_ - courier release order process because the item is not on any shelve

_[moved]_ - if the overflow shelf is full, this action happens when is possible to move some item to the right temp shelf and put the upcoming order on overflow

_[gone]_ - when the courier look if his order was on the pickup area and it was not there

_[discarded]_ - when the movement between shelves is not possible, a random item from overflow is discarded

_[delivered]_ - when the courier delivers the order.

## Customizing simulation

The architecture was made to change the simulation parameters easily.

### Changing basic parameters

```python
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

```

Definition:
_RANDOM_SEED_ - seed to reproduce the data given by a pseudo-random and get the same result

_INTERVAL_ORDERS_ = Interval between orders. ex. 0.5 = 2orders/s

_MIN_COURIER_TIME_ = Minimum time to courier arrive to get the order on pickup area

_MAX_COURIER_TIME_ = Max time to courier arrive to get the order on pickup area

_OVERFLOW_DECAY_MODIFIER_ = Modifier that multiplies order value formula to decay faster when they are in overflow shelf.

_factor_ = Simulation velocity.

### Changing Shelves structure:

The structure of the shelves Coordinator was designed to be is flexible. It is possible to add many shelves as you can with any capacity. Moreover, It is possible to change the full-stack overflow behavior, just sending another function on the constructor. I did that way to build the full-stack overflow logic increasingly with TDD.

```python
def main():
    orders = get_initial_orders()
    core = CKitchen(orders, parameters=parameters, factor=1)
    coordinator = ShelvesCoordinator(core, overflow_capacity=1, overflowFullFunc=discard_full_overflow)
    coordinator.addShelf('hot', 1)
    coordinator.addShelf('frozen', 1)
    core.setCoordinator(coordinator)
    core.simulate()
    core.run()

```


## Test Coverage:

![Coverage test report](./src/resources/report.png)
