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

$ mpiexec.mpich -n 1 -usize 3 python run.py

$ python run.py

"""

import time

from core_functions import distribute_tasks

#
def example_task(task, **kwargs):

    time.sleep(3)

    return task


# black codecov

if __name__ == "__main__":

    tasks = range(5)

    rslt = distribute_tasks(example_task, tasks, num_cores=3, distributed=True)

    # clickup
