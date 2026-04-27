students = [
    {"name": "Baljeet", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 48},
    {"name": "David", "grade": 30},
    {"name": "Eve", "grade": 44}
]
for i, student in enumerate(students, start=1):
    if student["grade"] >= 50:
        print(f"{i}. {student['name']} - {student['grade']} - Pass")
    else: 
        print(f"{i}. {student['name']} - {student['grade']} - Fail")
        