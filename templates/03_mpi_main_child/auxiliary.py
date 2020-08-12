from enum import IntEnum
import shutil
import glob

import pandas as pd


Tags = IntEnum('Tags', 'READY START DONE EXIT')


def aggregate_results():

    dfs = list()
    for subdir in glob.glob("subdir_child_*"):
        rank = subdir.split("_")[-1]
        df = pd.read_pickle(f"{subdir}/rslt_child_{rank}.pkl")
        df["rank"] = rank
        dfs.append(df)
    rslt = pd.concat(dfs, axis=0, ignore_index=True)
    rslt.index.name = "sample"
    rslt.to_pickle("rslt_main.pkl")
    [shutil.rmtree(dirname) for dirname in glob.glob("subdir_child_*")]

    return rslt
