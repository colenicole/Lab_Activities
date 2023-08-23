# program to display student's marks from record
student_name = "elsa"

marks = {"James" : 90, "Jules" : 55, "Arthur" : 77}

for students in marks:
    if students == student_name:
        print(marks[student])
        break
else:
    print("No entry with that name found.)