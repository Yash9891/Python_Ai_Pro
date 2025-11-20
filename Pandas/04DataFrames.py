# DataFrame= A tabular data structure with rows and columns - 2D

import pandas as pd

data = {"Name": ["Songe", "Patrick", "Squid"], "Age": [30, 35, 50]}

df = pd.DataFrame(data, index=["Emp1", "Emp2", "Emp3"])


# add a new column
df["Job"] = ["cook", "fresher", "cashier"]

# print(df.loc["Emp1"])
# print(df.iloc[1])

# add a new row
new_rows = pd.DataFrame(
    [
        {"Name": "Sandy", "Age": 23, "Job": "Engineer"},
        {"Name": "Pjin", "Age": 43, "Job": "Manager"},
    ],
    index=["Emp4", "Emp5"],
)
df = pd.concat([df, new_rows])


print(df)
