import os

import numpy as np

from core_functions import distribute_tasks


def example_func(x):
    return x


def get_random_request():

    num_tasks = np.random.randint(5, 25)
    num_cores = np.random.randint(1, num_tasks)

    # We need to check whether MPI was set up before running the test battery. There is no
    # standardized way of doing so according to
    if "PMI_SIZE" not in os.environ.keys():
        is_distributed = False
    else:
        is_distributed = np.random.choice([True, False])

    tasks = range(num_tasks)

    return tasks, num_cores, is_distributed


def test_1():
    distribute_tasks(example_func, *get_random_request())
