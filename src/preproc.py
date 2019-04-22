import os
from pandas import read_csv

file_dir = "../data/additional_files"

dataframes = {}

for filename in os.listdir(file_dir):
    name = filename.split(".")[0] # cut out '.dat' extension
    path = f"{file_dir}/{filename}"
    print(f"Preprocessing {name}...")
    with open(path, encoding="utf-8", errors="backslashreplace") as fileObj:
        dataframes[name] = read_csv(fileObj, sep=None, engine="python", error_bad_lines = False, warn_bad_lines=False)

print("Dataframe Shapes:")

for key in dataframes.keys():
    print(f"\t{key}: {dataframes[key].shape}")
