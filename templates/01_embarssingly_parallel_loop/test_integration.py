"""Integration tests.

This module contains the integration tests that all the individual units are combined and tested
together.

"""
from functools import partial
import os

import numpy as np
import pytest

from core_functions import distribute_tasks


def example_func(x):
    return x


def get_random_request():
    """Random test case.

    This function sets up a random test case that differs depending on whether MPI capabilities
    are available or not.

    """
    num_tasks = np.random.randint(5, 25)
    num_proc = np.random.randint(1, num_tasks)

    # We need to check whether MPI was set up before running the test battery. There is no
    # standardized way of doing so according to
    if "PMI_SIZE" not in os.environ.keys():
        is_distributed = False
    else:
        is_distributed = np.random.choice([True, False])

    tasks = range(num_tasks)

    return tasks, num_proc, is_distributed


@pytest.mark.repeat(10)
def test_1():
    """Test a random request.

    This test simply evaluates a random request. It automatically checks whether a distributed
    evaluation is an option.

    """
    distribute_tasks(example_func, *get_random_request())


@pytest.mark.repeat(10)
def test_2():
    """Varying the number of processes.

    This test evaluates the same request with different number of processes and ensures that the
    amount resources do not matter for the results.

    """

    tasks, num_proc, is_distributed = get_random_request()

    p_distribute_tasks = partial(distribute_tasks, example_func, tasks)
    rslts = [p_distribute_tasks(resource) for resource in [1, num_proc]]

    np.testing.assert_equal(*rslts)


@pytest.mark.repeat(10)
@pytest.mark.mpi
def test_3():
    """Alternating between shared and distributed memory.

    This test evaluates the same request using the ``multiprocessing`` and ``mpi4py`` library and
    ensures that both yield the same result.

    """
    tasks, num_proc, _ = get_random_request()

    p_distribute_tasks = partial(distribute_tasks, example_func, tasks, num_proc)
    rslts = [p_distribute_tasks(is_distributed) for is_distributed in [True, False]]

    np.testing.assert_equal(*rslts)
