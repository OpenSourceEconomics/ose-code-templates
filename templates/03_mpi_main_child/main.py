import glob
import shutil
import sys
import os

# In this script we only have explicit use of MPI as our level of parallelism. This needs to be
# done right at the beginning of the script.
update = {'NUMBA_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1',
          'NUMEXPR_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1'}
os.environ.update(update)

import numpy as np
import pandas as pd

from mpi4py import MPI


import chaospy as cp

status = MPI.Status()

num_sample = 4
num_child = 2

# TODO: Special case where num_sample = num_rprocs

"""We create our samples here as a numpy array. This is the fastest alternative"""
distribution = cp.J(cp.Uniform(0.92, 0.98), cp.Uniform(0.03, 0.08))
samples = distribution.sample(num_sample, rule="random").T

num_params = samples.shape[1]

info = MPI.Info.Create()
info.update({"wdir": os.getcwd()})


# We need all child processes to work in a separate directory.
[shutil.rmtree(dirname) for dirname in glob.glob("subdir_child_*")]
file_ = os.path.dirname(os.path.realpath(__file__)) + '/child.py'
comm = MPI.COMM_SELF.Spawn(sys.executable, args=[file_], maxprocs=num_child, info=info)

# We send all problem-specific information once and for all.
prob_info = dict()
prob_info["num_params"] = num_params
prob_info["num_sample"] = num_sample
comm.bcast(prob_info, root=MPI.ROOT)

check_in = np.zeros(1, dtype='float64')
cmd = dict()
cmd['terminate'] = np.array(0, dtype='int64')
cmd['execute'] = np.array(1, dtype='int64')

for sample in samples:

    sample = np.array(sample, ndmin=2)

    comm.Recv([check_in, MPI.DOUBLE], status=status)
    rank_sender = status.Get_source()

    comm.Send([cmd['execute'], MPI.INT], dest=rank_sender)

    sample = np.array(sample, dtype="float64")
    comm.Send([sample, MPI.DOUBLE], dest=rank_sender)

# We are done and now terminate all child processes properly and finally the turn off the
# communicator.
[comm.Send([cmd['terminate'], MPI.INT], dest=rank) for rank in range(num_child)]
comm.Disconnect()

# We aggregate all dataframes into a single file.
dfs = list()
for subdir in glob.glob("subdir_child_*"):
    rank = subdir.split("_")[-1]
    df = pd.read_pickle(f"{subdir}/rslt_child_{rank}.pkl")
    df["rank"] = rank
    dfs.append(df)
rslt = pd.concat(dfs, axis=0).reset_index()
rslt.to_pickle("rslt_main.pkl")
