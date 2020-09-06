import pandas as pd
import os

def combine_Enet_and_Atomic():
    path = "data/enet/"
    atomic_path = "data/atomic/"
    combine_path = "data/combine/"
    filelist = os.listdir(path)
    filelist = list(filter(lambda x:x[-4:] == ".csv"))

    for file in filelist:
        sp = file.split("_")[-1].strip(".csv")
        enet_df = pd.read_csv(path+file)
        atomic_df = pd.read_csv(atomic_path+f"v4_atomic_{sp}.csv")
        combine_df = pd.concat([atomic_df, enet_df])
        combine_df.to_csv(combine_path+ f"combine_{sp},csv")