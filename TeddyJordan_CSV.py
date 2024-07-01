import csv

def input_student_data():
    students = []
    num_students = int(input("Enter number of students: "))

    for _ in range(num_students):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter student's grade for Exam 1: "))
        exam2 = int(input("Enter student's grade for Exam 2: "))
        exam3 = int(input("Enter student's grade for Exam 3: "))
        students.append([first_name, last_name, exam1, exam2, exam3])

    return students

def write_to_csv(students, filename='grades.csv'):
    header = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students)

if __name__ == "__main__":
    students = input_student_data()
    write_to_csv(students)
    print(f"Data has been written to {filename}")