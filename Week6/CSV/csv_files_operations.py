import csv

with open("Week6/CSV/students.csv", "r", newline="", encoding="utf-8") as file:
    # newline="" is essential to prevent extra blank lines on Windows
    reader1 = csv.reader(
        file
    )  # reader stores the content of the csv file in a list format

    # Without skipping the header
    for row in reader1:
        print(row)
    print()

    file.seek(0)  # This is done to reset the pointer to the start of the file

    # Skipping the header
    next(reader1)
    for row in reader1:
        print(row)
    print()

    file.seek(0)  # This is done to reset the pointer to the start of the file
    reader2 = csv.DictReader(
        file
    )  # reader stores the content of the csv file in a dictionary format
    for row in reader2:
        print(row)
    print()

    file.seek(0)  # This is done to reset the pointer to the start of the file
    next(reader2)  # Skipping the header
    for row in reader2:
        print(row["name"] + ", " + row["grade"])

# Creating data to be written in a csv file
rows = [["Alice", "A"], ["Bob", "B"], ["Charlie", "C"]]
with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Writing single rows
    writer.writerow(["Name", "Grade"])

    # Writing multiple rows
    writer.writerows(rows)

dict_data = [
    {"name": "Alice", "age": 23, "country": "USA"},
    {"name": "Bob", "age": 24, "country": "USA"},
    {"name": "Charlie", "age": 25, "country": "USA"},
]

with open("output2.csv", "w", newline="", encoding="utf-8") as file:
    labels = ["name", "age", "country"]
    writer = csv.DictWriter(file, fieldnames=labels)

    writer.writeheader()  # Write the header row
    writer.writerows(dict_data)
