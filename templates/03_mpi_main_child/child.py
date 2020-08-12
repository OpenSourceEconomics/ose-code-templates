#!/usr/bin/env python
"""This script provides all capabilities for the child processes."""
import pickle as pkl
import shutil
import glob
import os

import pandas as pd
import numpy as np
import respy as rp

from mpi4py import MPI

comm = MPI.Comm.Get_parent()
num_slaves, rank = comm.Get_size(), comm.Get_rank()

subdir = f"subdir_child_{rank}"
os.mkdir(subdir)
os.chdir(subdir)

# We now set up the simulation function of  `respy` and receive some task-specific information.
params, options, df = rp.get_example_model("robinson_crusoe_basic")
simulate = rp.get_simulate_func(params, options)


prob_info = comm.bcast(None, root=0)

rslt = list()
while True:
    # Signal readiness
    comm.Send([np.zeros(1, dtype="float64"), MPI.DOUBLE], dest=0)

    cmd = np.array(0, dtype="int64")
    comm.Recv([cmd, MPI.INT], source=0)

    #
    if cmd == 0:
        print("done")
        comm.Disconnect()
        break

    elif cmd == 1:
        # We are called to sample the quantity of interest and need to update the parameters
        # accordingly.
        sample = np.array([0.0, 0.0], dtype="float64")
        comm.Recv([sample, MPI.DOUBLE], source=0)

        # params.loc["delta", "value"], params.loc[("wage_a", "exp_edu"), "value"] = sample
        params.loc["delta", "value"], params.loc[("wage_fishing", "exp_fishing"), "value"] = sample
        stat = simulate(params).groupby("Identifier")["Experience_Fishing"].max().mean()
        rslt.append([stat, *sample])
    else:
        raise AssertionError

# We set up a container to store the results.
df = pd.DataFrame(rslt, columns=["qoi", "delta", "exp_edu"])
df.index.name = "sample"
df.to_pickle(f"rslt_child_{rank}.pkl")
