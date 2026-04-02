# Accessing nested dictionaries
students = {"ram": {"math": 90, "science": 80}, "krishna": {"math": 95, "science": 85}}
print(students["krishna"]["science"])

# Adding new entries to nested dictionaries
students["ram"]["english"] = 88
print(students["ram"])

# Iterating through nested dictionaries
for student, subjects in students.items():
    for subject, score in subjects.items():
        print(f"{student} scored {score} in {subject}")

# Using if statements to check for specific conditions
students = {
    "ram": {"math": 90, "science": 80},
    "krishna": {"math": 60, "science": 50},
    "arjun": {"math": 85, "science": 88},
}
filtered = {
    student: subjects
    for student, subjects in students.items()
    if all(score >= 70 for score in subjects.values())
}
print(filtered)

# Average marks
avg = {
    student: sum(subjects.values()) / len(subjects)
    for student, subjects in students.items()
}
print(avg)

# Flattening nested dictionaries
flattened = {
    f"{student}_{subject}": marks
    for student, subjects in students.items()
    for subject, marks in subjects.items()
}
print(flattened)
