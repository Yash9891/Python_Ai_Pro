# series = A pandas 1 Dimentional labeled array that can hold any data type
# think of it like a single column in excel

import pandas as pd

data = [100.1, 102.2, 104.3, 400]
# data = ["a", "b", "c"]

series = pd.Series(
    data, index=["a", "b", "c", "e"]
)  # you can cretate your own lables-index

# update valuse
series.loc["c"] = 9999
# access valuse directly from series by labels
print(series.loc["a"])

# acces valuse from index
print(series.iloc[2])

# print(series)

# return series value>200
print(series[series > 200])
