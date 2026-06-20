# Student Marks Dictionary

students = {
    "Ramjoth": 85,
    "Aditya": 92,
    "Tanmay": 78,
    "Rishi": 88,
    "Darshan": 95
}

print("Student Details:")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

print("Class Average =", average)

topper = max(students, key=students.get)

print("Highest Marks Student =", topper)
print("Marks =", students[topper])
