number_of_students = int(input())

student_records = {}
for _ in range(number_of_students):
    name, grade = input().split()
    if name not in student_records.keys():
        student_records[name] = []
    student_records[name].append(float(grade))


for student, grades in student_records.items():
    print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {sum(grades) / len(grades):.2f})")