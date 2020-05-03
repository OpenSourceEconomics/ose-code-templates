import time
import os

from core_functions import distribute_tasks

# TODO: As instructions

# We want to ensure all automatic parallelism is turned off.
update = {
    "NUMBA_NUM_THREADS": "1",
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
}
os.environ.update(update)

def example_task(task, **kwargs):

    time.sleep(3)

    return task

# black codecov

if __name__ == "__main__":

    tasks = range(32)

    rslt = distribute_tasks(example_task, tasks, num_cores=10, distributed=True)


    #clickup

    # distributed/shared as options, have a function run_tasks, that than either runs

    # RUN CHECKS FOR DISTRIBUTED AT PARSE OF CLI
    # TODO: There was an issue with tasks smaller than resources, check!