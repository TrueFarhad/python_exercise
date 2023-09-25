import csv
with open('./students_grades.csv') as student:
    reader = csv.reader(student)
    for grades in reader:
        student_grade = (grades[1:])
        grade_sum = (sum(int(grade) for grade in student_grade))
        average = grade_sum/len(student_grade)
        print(average)