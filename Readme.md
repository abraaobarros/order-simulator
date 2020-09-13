# Engineering Challenge Homework

Discrete-Event Simulation of delivery centrilized kitchen. For this test, I choose python with simpy to simulate the enviroument and run the realtime simulation.
I found on simpy a simple use of python generators to solve resources concurrence problem. I used just Resources, Events and Enviroment as a foundation of our model.

You can find simpy documentation at this link: https://simpy.readthedocs.io/en/latest/

# Installation:

### Quickstart:

Run it inside folder project. Make sure you are using python 3.6+

```python
pip install -r requirements.txt

```

Run it on terminal:

```python

python main.py

```

So, this should be enough to run the project and start the simulation:
![First run](./src/resources/report.png)

    requirements python3

    pip install ./

    basic run
    ckitchen

```
ckitchen --interval_orders 0.5 --max_courier_time 6 --min_courier_time 2 --overflow_decay_modifier 2 --normal_decay 1

```

## Test Coverage:

![Coverage test report](./src/resources/report.png)
