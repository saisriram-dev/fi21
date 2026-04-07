import pandas as pd

df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["A", "B", "C"]})

df2 = pd.DataFrame({"ID": [1, 2, 4], "Marks": [90, 80, 70]})

# Merging the two dataframes on the 'ID' column

# Inner merge: Only rows with matching IDs in both dataframes will be included in the result.
merged1 = pd.merge(df1, df2, on="ID", how="inner")
print(merged1)
print()

# Left merge: All rows from the left dataframe (df1) will be included in the result,
# and matching rows from the right dataframe (df2) will be included.
# If there is no match, NaN values will be filled in for the right dataframe's columns.
merged2 = pd.merge(df1, df2, on="ID", how="left")
print(merged2)
print()

# Right merge: All rows from the right dataframe (df2) will be included in the result,
# and matching rows from the left dataframe (df1) will be included.
# If there is no match, NaN values will be filled in for the left dataframe's columns.
merged1 = pd.merge(df1, df2, on="ID", how="right")
print(merged1)
print()

# Outer merge: All rows from both dataframes will be included in the result.
# If there is no match, NaN values will be filled in for the columns of the
# dataframe that does not have a match.
merged1 = pd.merge(df1, df2, on="ID", how="outer")
print(merged1)
print()
