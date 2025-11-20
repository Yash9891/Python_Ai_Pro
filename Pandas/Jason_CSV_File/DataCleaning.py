"""
Data cleaning =The process of fixing/removing:
incomplete data, incorrect data.
&5% of work done with pandas is data cleaning
"""

import pandas as pd

df = pd.read_csv("Pandas/Jason_CSV_File/sample_data2.csv")

# Drop irrelevant column-------------------------------------

# df = df.drop(columns=["attack", "id"])

# Handel missing data----------------------------------------
# df = df.dropna(subset=["type"])  # remove if NA (na)

# replace the NA valuse with None------------------------------
# df = df.fillna({"type": "None"})

# Fix inconsistent values------------------------------
# df["type"] = df["type"].replace({"Fire": "FIRE", "Water": "WATER"})

# Make the name col in lowercase- standardize text-----------------------------
# df["name"] = df["name"].str.lower()


# fix the data types: convert attack col into float------------------------
# df["attack"] = df["attack"].astype(float)

# Remove duplicates entries---------------------------------------
df = df.drop_duplicates()
print(df)
