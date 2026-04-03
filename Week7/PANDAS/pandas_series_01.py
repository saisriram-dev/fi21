import pandas as pd

""" Series is a one-dimensional labeled array capable of holding any data type 
    (integers, strings, floating point numbers, Python objects, etc.). The axis labels are 
    collectively referred to as the index. We can think of them like a column in an Excel spreadsheet.
    The cilums have an index and a value. The index is the label for the value, and the value is the 
    data stored in the series."""

data = [100, 102, 104]

series = pd.Series(data)
print(series)
print()
""" 
    The output of the above code will be:
    0    100
    1    102
    2    104
    dtype: int64
    
    The output shows the index (0, 1, 2) and the corresponding values (100, 102, 104). 
    The dtype indicates that the data type of the values is int64.
"""

# To set custom index for the series, we can pass a list of labels to the index parameter
data2 = [100, 102, 104, 200, 202]
series2 = pd.Series(data2, index=["a", "b", "c", "d", "e"])

# To search and access values in the series, we can use the index labels
print(series2["a"])  # Output: 100
print(series2["d"])  # Output: 200
print()

# We can also use the .loc accessor to access values by index labels
# loc stands for location by label, and it allows us to access values based on their index labels
print(series2.loc["a"])  # Output: 100
print(series2.loc["d"])  # Output: 200
print(series2.loc[["a", "d"]])
print() 
#  Output: a    100
#          d    200
#          dtype: int64

# We can also use the .iloc accessor to access values by integer position
# This is just like accessing values in a list or array, where we use the integer position to access the value
print(series2.iloc[0])  # Output: 100
print(series2.iloc[3])  # Output: 200
print(series2.iloc[[0, 3]])
print()
# Output: a    100
#         d    200
#         dtype: int64

# We can also perform operations on the series, such as addition, subtraction, multiplication, and division
# When we perform operations on a series, the operation is performed element-wise, meaning that the operation is 
# performed on each element of the series individually
series3 = series2 + 10
print(series3)
print()
# Output: a    110
#         b    112
#         c    114
#         d    210
#         e    212
#         dtype: int64

# Modifying values in the series
series2["a"] = 150
series2.loc["d"] = 250
series2.iloc[1] = 123
print(series2)
print()

# Filtering values in the series
filtered_series = series2[series2 % 2 == 0]  # This will filter out the values that are even
print(filtered_series)
print()
"""
a    150
c    104
d    250
e    202
dtype: int64
"""

# We needn't store the filtered series in a new variable, we can directly print the filtered values
print(series2[series2 < 200])
