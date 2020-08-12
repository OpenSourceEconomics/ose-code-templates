import shutil
import glob
import sys
import os

if "PMI_SIZE" not in os.environ.keys():
    raise AssertionError("requires MPI access")
from mpi4py import MPI

import chaospy as cp
import numpy as np

from auxiliary import aggregate_results
from auxiliary import TAGS


if __name__ == "__main__":

    # We specify the number of draws and number of children.
    num_samples, num_children = 5, 2

    # We draw a sample from the joint distribution of the parameters that is subsequently
    # distributed to the child processes.
    distribution = cp.J(cp.Uniform(0.92, 0.98), cp.Uniform(0.03, 0.08))
    samples = distribution.sample(num_samples, rule="random").T

    info = MPI.Info.Create()
    info.update({"wdir": os.getcwd()})

    # We start all child processes and make sure they can work in their own respective directory.
    [shutil.rmtree(dirname) for dirname in glob.glob("subdir_child_*")]
    file_ = os.path.dirname(os.path.realpath(__file__)) + "/child.py"
    comm = MPI.COMM_SELF.Spawn(
        sys.executable, args=[file_], maxprocs=num_children, info=info
    )

    # We send all problem-specific information once and for all.
    prob_info = dict()
    prob_info["num_params"] = samples.shape[1]
    comm.bcast(prob_info, root=MPI.ROOT)

    status = MPI.Status()
    for sample in samples:

        comm.recv(status=status)
        rank_sender = status.Get_source()

        comm.send(None, tag=TAGS.RUN, dest=rank_sender)

        sample = np.array(sample, dtype="float64")
        comm.Send([sample, MPI.DOUBLE], dest=rank_sender)

    # We are done and now terminate all child processes properly and finally the turn off the
    # communicator. We need for all to acknowledge the receipt to make sure we do not continue here
    # before all tasks are not only started but actually finished.
    [comm.send(None, tag=TAGS.EXIT, dest=rank) for rank in range(num_children)]
    [comm.recv() for rank in range(num_children)]
    comm.Disconnect()

    rslt = aggregate_results()
