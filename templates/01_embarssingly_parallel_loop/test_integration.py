import time
import os

import numpy as np

from core_functions import distribute_tasks


def example_task(task, **kwargs):

    # use evaluation of rosebvrock function here and in run.py
    time.sleep(1)

    return task


def get_random_request():

    num_tasks = np.random.randint(5, 25)
    num_cores = np.random.randint(1, num_tasks)

    # TODO: reference to hack stackoverflow
    if "PMI_SIZE" in os.environ.keys():
        is_distributed = np.random.choice([True, False])
    else:
        is_distributed = False

    tasks = range(num_tasks)

    return tasks, num_cores, is_distributed


def test_1():

    distribute_tasks(example_task, *get_random_request())
