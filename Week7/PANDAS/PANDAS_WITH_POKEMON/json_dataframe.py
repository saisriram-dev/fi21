import pandas as pd

df = pd.read_json("Week7\PANDAS\PANDAS_WITH_POKEMON\pokemon.json")

# Aggregate functions
print(
    f"Mean: {df.mean(numeric_only=True)}"
)  # It will return the mean of all the numeric columns in the dataframe.
print(
    f"Median: {df.median(numeric_only=True)}"
)  # It will return the median of all the numeric columns in the dataframe.
print(
    f"Mode: {df.mode(numeric_only=True)}"
)  # It will return the mode of all the numeric columns in the dataframe.
print(
    f"Standard Deviation: {df.std(numeric_only=True)}"
)  # It will return the standard deviation of all the numeric columns in the dataframe.
print(
    f"Variance: {df.var(numeric_only=True)}"
)  # It will return the variance of all the numeric columns in the dataframe.
print(
    f"Minimum: {df.min(numeric_only=True)}"
)  # It will return the minimum value of all the numeric columns in the dataframe.
print(
    f"Maximum: {df.max(numeric_only=True)}"
)  # It will return the maximum value of all the numeric columns in the dataframe.
print(
    f"Sum: {df.sum(numeric_only=True)}"
)  # It will return the sum of all the numeric columns in the dataframe.
print(
    f"Count: {df.count()}"
)  # It will return the the number of non-empty rows in each column of the dataframe. Null values will not be counted.

"""

.dropna() function is used to drop the rows with null values in the dataframe.
By default, it will drop the rows with any null values in any column, but we can also specify the 
subset of columns to check for null values using the subset parameter.

For example, if we want to drop the rows with null values in the 'Type 1' column, we can use 
the following code:
df['Type1'] = df.dropna(subset=['Type1'])
This will drop all the rows where the 'Type1' column has null values. 

If we want to drop the rows with null values in the 'Type 1' and 'Type 2' columns, we can use the 
following code:
df.dropna(subset=['Type1', 'Type2'])
This will drop all the rows where the 'Type1' or 'Type2' column has null values.

Axis parameter in dropna() function is used to specify whether to drop rows or columns with null values.
By default, axis=0, which means it will drop rows with null values.
If we want to drop columns with null values, we can set axis=1. For example:
df.dropna(axis=1)
This will drop all the columns where there is at least one null value in any row of that column

Threshold parameter in dropna() function is used to specify the minimum number of non-null values 
required to keep a row or column.
For example, if we want to drop rows that have less than 3 non-null values, 
we can use the following code:
df.dropna(thresh=3)

"""

# Fillna() function is used to fill the null values in the dataframe with a specified value.
df["Height"] = df["Height"].fillna(df["Height"].mean())
# It will replace the null values in the 'Height' column with the mean of the 'Height' column.
df = df.fillna(0)
# It will fill all the null values in the dataframe with 0.

# The above code will fill the null values in the 'Height' column.
# And it will replace the null values with the mean of the 'Height' column.
# The second line of code will fill all the null values in the dataframe with 0,
# so it will fill the null values in the 'Height' column with 0 as well,
# but since we have already filled the null values in the 'Height' column with the mean,
# it will not affect the 'Height' column because there are no null values in the 'Height' column
# after the first line of code.

""" 
    If we implement the second line of code first before the first line of code,
    then it will fill all the null values in the dataframe with 0,
    including the null values in the 'Height' column, so it will fill the null values in the 'Height'
    column with 0 as well, 
    and then when we implement the first line of code, it will not affect the 'Height' column 
    because there are no null values in the 'Height' column after the second line of code.
 """
