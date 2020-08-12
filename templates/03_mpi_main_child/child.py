#!/usr/bin/env python
"""This script provides all capabilities for the child processes."""

import os

# In this script we only have explicit use of MPI as our level of parallelism. This needs to be
# done right at the beginning of the script.
update = {
    "NUMBA_NUM_THREADS": "1",
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
}
os.environ.update(update)

from mpi4py import MPI
import pandas as pd
import numpy as np
import respy as rp

from auxiliary import TAGS


if __name__ == "__main__":
    comm = MPI.Comm.Get_parent()
    num_slaves, rank = comm.Get_size(), comm.Get_rank()
    status = MPI.Status()

    # We need some additional task-specific information.
    prob_info = comm.bcast(None)

    subdir = f"subdir_child_{rank}"
    os.mkdir(subdir)
    os.chdir(subdir)

    # We now set up the simulation function of  `respy` and receive some task-specific information.
    params, options, df = rp.get_example_model("kw_94_one")
    simulate = rp.get_simulate_func(params, options)

    rslt = list()
    while True:

        # Signal readiness
        comm.send(None, dest=0)

        # Receive instructions and act accordingly.
        comm.recv(status=status)
        tag = status.Get_tag()

        if tag == TAGS.EXIT:
            # We set up a container to store the results.
            df = pd.DataFrame(rslt, columns=["qoi", "delta", "exp_edu"])
            df.index.name = "sample"
            df.to_pickle(f"rslt_child_{rank}.pkl")

            # Now we are ready to acknowledge completion and disconnect.
            comm.send(None, dest=0)
            comm.Disconnect()
            break

        elif tag == TAGS.RUN:
            # We are called to sample the quantity of interest and need to update the parameters
            # accordingly.
            sample = np.empty(prob_info["num_params"], dtype="float64")
            comm.Recv([sample, MPI.DOUBLE])

            (
                params.loc["delta", "value"],
                params.loc[("wage_a", "exp_edu"), "value"],
            ) = sample

            stat = simulate(params).groupby("Identifier")["Experience_Edu"].max().mean()
            rslt.append([stat, *sample])

        else:
            raise AssertionError
