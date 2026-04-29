students = [
    {"name": "Baljeet", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 48},
    {"name": "David", "grade": 30},
    {"name": "Eve", "grade": 72}
]

def average_score(students):
    total = sum(student["grade"] for student in students)
    return total / len(students)

def print_report_card(students):
    print("====================================")
    print("Report Card".center(30))
    print("====================================")
    for i, student in enumerate(students, start=1):
        status = "Pass" if student["grade"] >= 50 else "Fail"
        print(f"{i}. {student['name']:<12} {student['grade']:<4} {status}")
    print("====================================")
    print(f"{'Average Score:':<14} {average_score(students):.2f}")
    print("====================================")

print_report_card(students)