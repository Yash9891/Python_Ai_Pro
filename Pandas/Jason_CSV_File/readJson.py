import pandas as pd

df = pd.read_json("Pandas/Jason_CSV_File/sample_data.json")
df = df.set_index("name")

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except:
    print(f"{pokemon} not found")
