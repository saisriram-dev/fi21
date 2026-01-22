from pathlib import Path

base = Path(__file__).parent
data2 = base/"data2"
data2.mkdir(exist_ok=True)

# To create a new file
# The following creates an empty file nd does nothing if it already exists
# After the file is created we can use the methods mentioned in the file_methods.py
file_path = data2/"myfile.txt"
file_path.touch(exist_ok=True)
print(file_path)

# A line is added to the file
with open(file_path, "a") as file:
    file.write("I want to be financially independent by 21")

# The file is read
with open(file_path, "r") as file:
    print(file.read()) # This will print the content of the file 
    print(file.read()) # This will print nothing as the pointer is already at the end of the file due to the above print statement
    
    # To know the position of the pointer
    print(file.tell())

    # To reset the pointer
    file.seek(0)
    
    # To move the pointer to a desired location we can use f.seek(offset, reference point)
    # Now we can again use the print function to display the content of the file for the second time

# File metadata
# It is mainly useful for logs, upload limits and cleanup scripts etc. 
stat = file_path.stat()
print(stat.st_size) # This will print the size of the file
print(stat.st_mtime) # This will print the time when the file was last modified
