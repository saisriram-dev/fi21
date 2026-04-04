import pandas as pd

df = pd.read_csv("Week7\PANDAS\PANDAS_WITH_POKEMON\pokemon.csv")

df["Is_Legendary"] = df["Legendary"].apply(lambda x: "Yes" if x else "No")

""" Another way to do the same thing is to use the function we defined below:
    def is_legendary(x):
        if x:
          return "Yes"
        else:
          return "No"
    df["Is_Legendary"] = df["Legendary"].apply(is_legendary)
"""

print(df)
