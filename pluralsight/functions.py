students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)
    
def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(name)


def run():
    student_list = get_students_titlecase()

    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    add_student(student_name, student_id)
    print_students_titlecase()

if __name__ == "__main__":
    run()