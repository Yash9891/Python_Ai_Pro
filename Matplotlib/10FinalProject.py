import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
df = pd.read_csv("Matplotlib/data.csv")

# create bar chart to show type 1 category- fire, water type
# print(df["Type1"].value_counts())

type_count=df["Type1"].value_counts(ascending=True) # to reverse the barchart
plt.barh(type_count.index, type_count.values, color="orange", edgecolor="red")
plt.title("Pokemon by Type")
plt.xlabel("Count")
plt.ylabel("Type")

# To fit everything with in a figure
plt.tight_layout()
plt.show()

# Print the DataFrame
# print(df)
