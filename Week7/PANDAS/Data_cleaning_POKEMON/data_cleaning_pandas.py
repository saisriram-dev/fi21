import pandas as pd

df = pd.read_csv("Week7/PANDAS/Data_cleaning_POKEMON/pokemon.csv", index_col="Name")

# 1. Dropping irrelevant columns
# We are dropping the 'No' and 'Legendary' columns as they are not relevant for our analysis.
df = df.drop(columns=["No", "Legendary"])

# 2. Handling missing data
# df = df.dropna(subset=["Type2"])  # Dropping rows where 'Type2' is null
df = df.fillna({"Type2": "None"})  # Filling null values in 'Type2' with 'None'
""" The above code will replace all the null values in the 'Type2' column with the string 'None'. 
    This way, we can keep all the rows in the dataframe while still indicating that there is no 
    secondary type for those Pokémon.
    
    Syntax: df = df.fillna({column_name: value_to_fill})
                        (or)
            df[column_name] = df[column_name].fillna(value_to_fill)

"""

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Fire": "FIRE"})
df["Type1"] = df["Type1"].replace({"Water": "WATER", "Grass": "GRASS"})

# 4. Standardize text
df["Name"] = df["Name"].str.lower()  # Converting all names to lowercase
# Other methods:
# df["Name"] = df["Name"].str.upper()  # Converting all names to uppercase
# df["Name"] = df["Name"].str.title()  # Converting all names to title case (first letter capitalized)

# 5. Handling duplicates
df = df.drop_duplicates()  # Dropping duplicate rows based on all columns
""" 
    If we want to drop duplicates based on a specific column, we can use the subset parameter:
    df = df.drop_duplicates(subset=["Name"])  # Dropping duplicate rows based on the 'Name' column
    
    Axis parameter in drop_duplicates() function is used to specify whether to drop duplicate rows or columns.
    By default, axis=0, which means it will drop duplicate rows.
    If we want to drop duplicate columns, we can set axis=1. 
    For example:
    df = df.drop_duplicates(axis=1)  # Dropping duplicate columns based on all rows
"""
