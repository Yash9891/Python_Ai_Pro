import pandas as pd

# aggregate fun: reduces a set of values into a single sumarry value: used with groupby() fun

df = pd.read_csv("Pandas/Jason_CSV_File/sample_data2.csv", index_col="name")


# Whole dataframe----------------------------------------
# # Average of each col - numeric only
# print(df.mean(numeric_only=True))

# # sum
# print(df.sum(numeric_only=True))

# # min
# print(df.min(numeric_only=True))

# # max
# print(df.max(numeric_only=True))

# # count-rows
# print(df.count())

# # Single col-----------------------------------------------
# # Average of each col - numeric only
# print(df["attack"].mean(numeric_only=True))

# # sum
# print(df["defense"].sum(numeric_only=True))

# # min
# print(df["defense"].min(numeric_only=True))

# # max
# print(df["defense"].max(numeric_only=True))

# # count-rows
# print(df["defense"].count())


# Groupby()-----------------------------------------

group = df.groupby("type")
print(group["attack"].mean())
print(group["attack"].sum())
print(group["attack"].count())
