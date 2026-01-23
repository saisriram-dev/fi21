import shutil
from pathlib import Path

address = str(input("Enter the path for the folder you want to organize: "))
base = Path(address)

# Creating a folder to store text documents
txt_folder = base/"Text Documents"
txt_folder.mkdir(exist_ok=True)

# Creating a folder to store pdf documents
pdf_files = base/"PDF files"
pdf_files.mkdir(exist_ok=True)

# Creating a folder to store image documents
img_files = base/"Image files"
img_files.mkdir(exist_ok=True)

for item in base.iterdir():
    if item.suffix == ".txt":
        print(f"Moving {item.name} to the created text documents folder...") # .name is a method that returns the name of the file instead of the full path address
        shutil.move(item, txt_folder)
        print("Done!")
    elif item.suffix == ".pdf":
        print(f"Moving {item.name} to the created pdf documents folder...")
        shutil.move(item, pdf_files)
        print("Done!")
    elif item.is_dir():
        print(f"{item.name} is a directory and can't be sorted in any of the created directories. Skipping...")
        print(f"Skipped sorting {item.name}!")
    elif item.suffix in {".jpg", ".png", ".jpeg", ".gif"}:
        # elif item.suffix == ".jpg" or item.suffix == ".png" or item.suffix == ".jpeg" or item.suffix == ".gif":
        # The above is a bad practice to write multiple or conditions in a single line
        print(f"Moving {item.name} to the created image documents folder...")
        shutil.move(item, img_files)
        print("Done!")
    else:
        print(f"Can't sort the item: {item.name} into any of the following categories: Text documents, PDF files, Image files")
        print(f"Skipping sorting for {item.name}")
        print("Skipped!")

print("Finished oraganizing your files into their respective folders!")
