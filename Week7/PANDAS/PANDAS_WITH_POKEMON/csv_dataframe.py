# Aggregate functions are in json_dataframe.py file, so we will not be using them in this file,
# but we will be using some of the other functions that are not aggregate functions.
import pandas as pd

df = pd.read_csv("Week7\PANDAS\PANDAS_WITH_POKEMON\pokemon.csv", index_col="Name")
"""
The index_col parameter sets all the values in the specified column in our case it's 'Name' as the 
index instead of the default numeric index. So instead of having 0, 1, 2, 3, ... as the index, 
we will have the names of the Pokemon as the index. So we lose the 'Name' column from the dataframe and 
it becomes the index of the dataframe.

If we only use index=[], we need to give 150 rows of indices for each row in the dataframe, 
otherwise it will return an error because it will not be able to assign the indices to the rows.
"""

""" If we use print(df) it will only show us the first and last 5 rows, 
    but if we use print(df.to_string()) it will show us all the rows and columns.
    If we have a large dataset, it is not recommended to use print(df.to_string()) 
    because it will print all the data and it can be overwhelming.
    
    Also if there is a gap or missing data for a particular column, 
    it will show as NaN (Not a Number) in the output in that specific location.
"""
print(df.to_string())
print()

# Head and Tail functions
print(df.head())  # It will show the first 5 rows of the dataframe.
print()

print(df.tail())  # It will show the last 5 rows of the dataframe.
print()

print(df.head(10))  # It will show the first 10 rows of the dataframe.
print()

print(df.tail(10))  # It will show the last 10 rows of the dataframe.
print()

# Info function
print(df.info())
print()
""" It will show us the summary of the dataframe, 
    including the number of non-null values in each column, the data type of each column, 
    and the memory usage of the dataframe.
"""

# Describe function
print(
    df.describe()
)  # It will show us the statistical summary of the numeric columns in the dataframe.
print()

# --------------------------- Columns ----------------------------
# To get the column names of the dataframe
print(df.columns)
print()

# To get the number of columns in the dataframe
print(len(df.columns))
print()

# Selecting a specific column from the dataframe
print(
    df["Height"]
)  # Truncated version of the column, it will only show the first and last 5 rows of the column.
print()

print(df["Height"].to_string())  # It will show all the rows of the column.
print()

print(
    df[["No", "Height", "Weight"]].to_string()
)  # It will show all the rows of the selected columns.
print()

# Adding a new column to the dataframe
""" 
df["New Column"] = ["Value 1", "Value 2", "Value 3"]
print(df.to_string())
print()
"""
# The above code will return an error because we are trying to add a new column with 3 values, but our dataframe has more than 3 rows.

# Adding a new column with the same value to all rows
df["New Column 2"] = "Value"
print(df.to_string())
print()
# The above code willn't return an error because we are adding a new column with the same value to all rows,
# so it will automatically fill the column with that value for all rows.
# but if we were to give a list of values to the new column, it should have the same number of values as
# the number of rows in the dataframe, otherwise it will return an error.

# --------------------------- Rows ----------------------------
# To get the number of rows in the dataframe
print(len(df))
print()

# To select a specific row from the dataframe
print(df.iloc[0])  # It will show the first row of the dataframe.
print()

print(df.iloc[0:5])  # It will show the first 5 rows of the dataframe (0, 1, 2, 3, 4).
print()

print(
    df.loc["Charizard":"Blastoise", ["Height", "Weight", "Legendary"]]
)  # It will show the first 6 rows of the selected columns.
print()

print(
    df.iloc[0:11:2, 0:3]
)  # It will show every alternate row from the first 11 rows and first 3 columns of the dataframe.
print()

print(
    df.iloc[0:5, [0, 3, 4]]
)  # It will show the first 5 rows and the columns at index 0, 3, and 4 of the dataframe.
print()

# Filtering the dataframe based on a condition
# When filtering the dataframe based on a condition, it will return a new dataframe that
# only contains the "rows" that satisfy the condition.
legendary_pokemon = df[df["Legendary"] == True]
print(legendary_pokemon.to_string())
print()

# Using or operator
ff_pokemon = df[(df["Type1"] == "Fire") | (df["Type2"] == "Flying")]
print(ff_pokemon.to_string())
print()
