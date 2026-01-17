# File handling in Python

# Open a file
# Beware: The 'w' method overwrites any existing content in a text file
# If a file like that doesn't exist it will be created while using the write and append methods
file_path1 = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/fi21/Week2/myfile.txt"
with open(file_path1, "w") as file:
    file.write("Hello world!")

# Append method will add the content to the end of the file not overwrite it
# If the file path does not exist it will be created
# If we run the program 2 times the content will be added twice
# However as the content is added twice there will be no spacing between the content
# So to add spacing we have to use \n or new line
# I ran this program 3 times so the content was added 3 times
file_path2 = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/fi21/Week2/names.txt"
with open(file_path2, "a") as file:
    file.write("\nMy name is P SAI SRI RAM")

# Read a file
# If the fiven file path doesn't exist it will throw an error
file_path3 = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/fi21/Week2/names2.txt"
with open(file_path3, "r") as file:
    content = file.read()
    print(content)

# Looping through a file
with open(file_path3, "r") as file:
    for line in file: # This will print each line of the text document
        print(line)

with open(file_path3, "r") as file:
    for line in file: # This will print each line of the text document
        # Use of .strip() is shown in the .strip screenshot in this directory
        print(line.strip(), end=", ") # This will ensure that there is a space between each name and no new lines
