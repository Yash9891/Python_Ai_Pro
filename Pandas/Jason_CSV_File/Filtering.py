import pandas as pd

df = pd.read_csv("Pandas/Jason_CSV_File/sample_data2.csv", index_col="name")

# filtering - keep the rows that match a condition

tall_pokemon = df[df["attack"] > 60]
powerFull_poki = df[df["defense"] > 80]
water_poki = df[df["type"] == "Water"]
defense_poki = df[(df["defense"] > 60) & (df["attack"] > 60)]
print(defense_poki)
