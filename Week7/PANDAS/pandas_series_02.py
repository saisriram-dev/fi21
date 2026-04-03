import pandas as pd

calories = {"Day 1": 1000, "Day 2": 2000, "Day 3": 900}
# In case of a dictionary, the keys are used as index and the values are used as data for the Series.
calories_series = pd.Series(calories)

# Accessing values in a Series can be done using the index labels or integer positions.
print(calories_series.loc["Day 1"])
print(calories_series[1])
print(calories_series["Day 3"])
print()

# Modifying values in a Series can be done using the index labels or integer positions.
calories_series.loc["Day 1"] += 100
print(calories_series.loc["Day 1"])
print()

calories_series.iloc[2] += 500
print(calories_series.iloc[2])
