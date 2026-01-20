# pathlib is a Python module for working with files and folders
# Path is a class from the pathlib module
# This line gives you the ability to represent files and folders as objects
from pathlib import Path

# The below folder may not exist. And the line doesn't create a folder
base = Path("data") # This line converts the string "data" into a Path object
# base now represents the path to the data folder in the current working directory because we are running the script from the root directory

# Creating a folder
"""This line creates a folder called "data" in the current working directory.
The exist_ok=True parameter is used to prevent an error if the folder already exists."""
base.mkdir(exist_ok=True) 

# Creating subfolders
"""This line creates a folder called "test" inside the "data" folder.
The exist_ok=True parameter is used to prevent an error if the folder already exists."""
# images = base / "images"
# images.mkdir(exist_ok=True) # This is one method to create a subfolder
# Always assign the subfolder to a variable only then can you do operations on the sub-folder
# like creating files and stuff using the variable name
images = (base/"images") # This is another method to create a subfolder
images.mkdir(exist_ok=True)

# Checking if something exists
# This is the first method
print(base.exists()) # Output: True
print(images.exists()) # Output: False
print((base/"images").exists()) # Output: True

# Here is a second method
Path(base).exists() # Output: True
Path(images).exists() # Output: False
Path(base/"images").exists() # Output: True

# Listing the files in a folder
# "." represents the current working directory i.e, Week2
# iterdir() is a method that returns an iterator over the entries in the directory
for file in Path(".").iterdir():
    print(file)

# Checking for files
for file in Path(".").iterdir():
    if file.is_file(): # This checks if the file is a regular file
        print(file)

# Checking for folders
for file in Path(".").iterdir():
    if file.is_dir(): # This checks if the file is a directory
        print(file)

# Deleting a folder
# (base/"images").rmdir()

# Deleting a file
# (base/"myfile.txt").unlink()

# Extensions check
for file in Path(".").iterdir():
    if file.suffix == ".txt":
        print(f"{file} is a text file!")
    elif file.is_dir():
        print(f"{file} is a directory!")
    else:
        print(f"{file} is not a text file!")
