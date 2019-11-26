students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)
    
def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(name)

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

def run():
    read_file()
    print_students_titlecase()
    
    adding_another = True
    
    while adding_another:
        student_list = get_students_titlecase()

        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")

        add_student(student_name, student_id)
        print_students_titlecase()
        
        adding = input("Do you want to add another student [Y/N] ").lower()
        
        if adding == "y":
            continue
            save_file(student_name)
        else:
            save_file(student_name)
            break


if __name__ == "__main__":
    run()