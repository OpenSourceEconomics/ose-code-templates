"""Docstring for the example.py module.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.


Notes
-----

There a lot of supporting material available online.

    https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html


Examples
-------

$ mpiexec -n 1 -usize 3 python run.py

$ python run.py

"""
from functools import partial

import numpy as np

from core_functions import distribute_tasks


def example_task(alpha, beta, gamma, x):

    x_ = np.array(x)
    result = alpha * (x_[1:] - x_[:-1] ** beta) ** gamma + (1 - x_[:-1]) ** gamma

    return result.sum()


if __name__ == "__main__":

    # We fix the details of our evaluation task and draw a sample of
    # evaluation points.
    num_points = 300
    num_inputs = 3

    total_draws = num_inputs * num_points
    eval_points = np.random.uniform(size=total_draws).reshape(num_points, num_inputs)

    # We partial out all function arguments that remain unchanged.
    alpha, beta, gamma = 100.0, 2.0, 3.0
    p_example_task = partial(example_task, alpha, beta, gamma)

    # We specify the amount and type of resources we have available and then
    # start the parallel evaluation of our test function.
    num_cores, is_distributed = 3, True
    distribute_tasks(p_example_task, eval_points, num_cores, is_distributed)
