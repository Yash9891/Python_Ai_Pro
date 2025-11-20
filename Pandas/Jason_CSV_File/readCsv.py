import pandas as pd

df = pd.read_csv("Pandas/Jason_CSV_File/sample_data2.csv", index_col="name")

# print(df.to_string())  # it will print every data


# Selection by column----------------

# print(df["name"])

# print(df["attack"])

# Select Multiple column------------------

# print(df[["name", "defense", "attack"]])


# Selct by rows-------------------------

# print(df.loc[0])

# print(df.loc["Pikachu"])

# select only col of pikachu------------------------
# print(df.loc["Pikachu", ["attack", "defense"]])

# select multiple rows-----------------------
# print(df.loc["Pikachu":"Charizard", ["attack", "defense"]])

# select by index-------------------------
# print(df.iloc[0:9:2, 0:3])  # 0:3    it means 1st 3 columns
