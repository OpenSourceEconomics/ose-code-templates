"""Core functions for template

Examples
--------
$ test
"""
import multiprocessing as mp
import os


def distribute_tasks(func_task, tasks, num_proc=1, is_distributed=False):

    # We might be able to save some resources.
    num_proc_intern = min(len(tasks), num_proc)

    if is_distributed:
        assert "PMI_SIZE" in os.environ.keys(), "MPI environment not available."
        from mpi4py.futures import MPIPoolExecutor

        executor = MPIPoolExecutor(num_proc_intern)

    else:
        executor = mp.Pool(num_proc_intern)

    with executor as e:
        rslt = list(e.map(func_task, tasks))

    return rslt
