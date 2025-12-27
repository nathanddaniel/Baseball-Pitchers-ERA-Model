import pandas as pd
import glob
import os

# merging files of all seasons for pitching data
rawSeasonCSV = glob.glob(os.path.join("data/raw", "pitching_*.csv"))

print(f"Found {len(rawSeasonCSV)} files:")
print(rawSeasonCSV)

if not rawSeasonCSV:
    print("No files found! Check your directory path and file names.")
else:
    # concatenating them into one dataframe
    completeRawDataFrame = pd.concat([pd.read_csv(f) for f in rawSeasonCSV], ignore_index=True)
    print(completeRawDataFrame)