import os
from pathlib import Path

base1 = "C:/Users/P SAI SRI RAM/OneDrive/Pictures"
base2 = "C:/Users/P SAI SRI RAM/OneDrive/Desktop/College"

# To list the contents of a directory
print(os.listdir(base1))

# To list the contents of a directory recursively
for roots, dirs, files in os.walk(base2):
    print(roots)
    print(dirs)
    print(files)

# To iterate in a folder using the Pathlib way
for item in Path(base2).iterdir():
    print(item)
