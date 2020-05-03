import multiprocessing as mp


# work with MPIEXEC mpich and openmpi

# I want educational resources
# run script without a problem using mpiexec or just standard python
# add link to ose-resources

#if 'PMI_SIZE' in os.environ.keys():
#    try:
#    except ImportError:
#        pass

# TODO: Wording num cores, num cpus?
# TODO: Set this up as decorator?
# args to task
def distribute_tasks(func_task, tasks, num_cores=1, distributed=False):

    # TODO: How assign resources to Pool?
    # Set up executor for tasks
    if distributed:
        from mpi4py.futures import MPIPoolExecutor
        executor = MPIPoolExecutor(num_cores)
    else:
        executor = mp.Pool(num_cores)

    with executor as e:
        rslt = list(e.map(func_task, tasks))

    return rslt










