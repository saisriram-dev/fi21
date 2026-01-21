from pathlib import Path

# To make any other folder than the working directory to be the base folder
# __file__ is a special variable that contains the path to the current file i.e pathlib_module2.py
# .parent is a method that returns the parent directory of the "__file__" i.e Week2
new_base = Path(__file__).parent
data2 = new_base/"data2"
data2.mkdir(exist_ok=True)

# To create a subfolder inside the data folder
images2 = data2/"images2"
images2.mkdir(exist_ok=True)

for item in new_base.iterdir():
    if item.is_dir():
        print(f"{item} is a directory!")
    else:
        suffix = item.suffix
        print(f"It is a file with suffix {suffix}")

for item in data2.iterdir():
    if item.is_dir():
        print(f"{item} is a directory!")
