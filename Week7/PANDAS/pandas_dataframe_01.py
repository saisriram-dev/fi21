# Dataframes in Pandas

import pandas as pd

# Dataframe = 2D labeled data, like an excel spreadsheet
data = {"Names": ["Spongebob", "Patrick", "Squidward"], "Age": [16, 17, 18]}

df = pd.DataFrame(data)  # Create a dataframe object
print(df)  # Print the dataframe
print()
"""
The output will be:
       Names  Age
0  Spongebob   16   
1    Patrick   17
2  Squidward   18

"""

# Changing the labels of the dataframe
df.index = ["Employee 01", "Employee 02", "Employee 03"]  # Change the index labels
# We could also do, df2 = pd.DataFrame(data, index=["Employee 01", "Employee 02", "Employee 03"])
print(df)
print()

# Accessing data in a dataframe
print(df["Names"])  # Access the "Names" column
print()

# Accessing a specific value in the dataframe
print(
    df["Names"]["Employee 01"]
)  # Access the value in the "Names" column for "Employee 01"
print()

print(df.loc["Employee 01"])  # Access the row for "Employee 01" using .loc
print()

print(df.iloc[0])  # Access the first row of the dataframe
print()

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add new rows
# Create a new datframe which consists as many dictionaries as the number of rows we want to add,
# and the keys of the dictionaries should be the same as the column names of the original dataframe.
new_row = pd.DataFrame(
    [
        {"Names": "Sandy", "Age": 19, "Job": "Scientist"},
        {"Names": "Mr. Krabs", "Age": 50, "Job": "Businessman"},
    ],
    index=["Employee 04", "Employee 05"],
)
df = pd.concat(
    [df, new_row]
)  # Concatenate the original dataframe with the new row dataframe
print(df)
print()
