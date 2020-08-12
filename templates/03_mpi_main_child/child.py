#!/usr/bin/env python
"""This script provides all capabilities for the child processes."""
import pickle as pkl
import numpy as np
import respy as rp

from mpi4py import MPI

comm = MPI.Comm.Get_parent()
num_slaves, rank = comm.Get_size(), comm.Get_rank()

print("hello", rank)

# We now set up the simulation function of  `respy` and receive some task-specific information.
#params, options, df = rp.get_example_model("kw_97_basic")
#simulate = rp.get_simulate_func(params, options)

prob_info = comm.bcast(None, root=0)

print(prob_info)

while True:
    # Signal readiness
    comm.Send([np.zeros(1, dtype="float64"), MPI.DOUBLE], dest=0)


    cmd = np.array(0, dtype="int64")
    comm.Recv([cmd, MPI.INT], source=0)

    x_free_econ_eval = np.tile(np.nan, 2)
    sendbuf = np.tile(np.nan, (num_slaves, 2))
    comm.Recv(sendbuf, x_free_econ_eval, source=0)

    print(x_free_econ_eval)

    if cmd == 0:
        print("done")
        comm.Disconnect()
        break

    elif cmd == 1:
        print('noting much to do')
        pass

    else:
        raise AssertionError