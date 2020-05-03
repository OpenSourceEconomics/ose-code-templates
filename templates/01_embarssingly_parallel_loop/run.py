"""Function evaluations in parallel.

This script performs numerous function evaluations in parallel. It showcases the seamless
switching between shared and distributed memory.

Notes
-----

These two books offer useful introductions to high-performance computing using Python.

    * Gorelick, M., & Ozsvald, I. (2014). "High performance Python: Practical performant programming for humans". O’Reilly Media.
    * Lanaro, G. (2017). "Python high performance: Build high-performing, concurrent, and distributed applications". Packt Publishing

There is also a lot of supporting material available online.

    * `Parallel programming with MPI for Python <https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html>`_
    * `Parallel Computing in Python using mpi4py <https://research.computing.yale.edu/sites/default/files/files/mpi4py.pdf>`_

Examples
--------

We provide two use cases below. In the first one the script is called using standard Python and
thus only shared memory parallelism is possible. The second one initializes an MPI environment,
which allows for distributed memory parallelism as well.

    $ python run.py

    $ mpiexec -n 1 -usize 3 python run.py

"""
from functools import partial

import numpy as np

from core_functions import distribute_tasks


def example_task(alpha, beta, gamma, x):
    x_ = np.array(x)
    result = alpha * (x_[1:] - x_[:-1] ** beta) ** gamma + (1 - x_[:-1]) ** gamma

    return result.sum()


if __name__ == "__main__":

    # We fix the details of our evaluation task and draw a sample of evaluation points.
    num_points, num_inputs = 300, 3

    total_draws = num_inputs * num_points
    eval_points = np.random.uniform(size=total_draws).reshape(num_points, num_inputs)

    # We partial out all function arguments that remain unchanged.
    alpha, beta, gamma = 100.0, 2.0, 3.0
    p_example_task = partial(example_task, alpha, beta, gamma)

    # We specify the amount and type of resources we have available and then start  the parallel
    # evaluation of our test function.
    num_proc, is_distributed = 3, True
    distribute_tasks(p_example_task, eval_points, num_proc, is_distributed)
