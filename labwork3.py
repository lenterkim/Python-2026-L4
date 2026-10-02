import math as m
import numpy as np


class Student:
    def __init__(self):
        self.id = -1
        self.Name = "Unknown"
        self.DoB = "Unknown"
        self.gpa = 0.0  # Thêm thuộc tính lưu gpa


class Course:
    def __init__(self):
        self.id = -1
        self.Name = "Unknown"
        self.credit = 0  # Sửa chính tả từ creadit thành credit


# Dictionary lưu điểm dạng: (course_id, student_id) -> mark
marks = {}


def student_population(students):
    return len(students)


def course_quantity(courses):
    return len(courses)


def add_student_info():
    stu = Student()
    stu.id = int(input("Student's id: "))
    stu.Name = input("Name: ")
    stu.DoB = input("DoB: ")
    return stu


def add_course_info():
    course = Course()
    course.id = int(input("Course's id: "))
    course.Name = input("Name of the course: ")
    course.credit = int(input("Credit: "))
    return course


def list_stu(students):
    if not students:
        print("There aren't any students on the list.")
        return
    print(f"\nTotal Students: {student_population(students)}")
    for i in students:
        print(f"Student Name: {i.Name} \nId: {i.id} \nDoB: {i.DoB}\n---")


def list_cour(courses):
    if not courses:
        print("There aren't any courses on the list.")
        return
    print(f"\nTotal Courses: {course_quantity(courses)}")
    for i in courses:
        print(f"Course ID: {i.id} \nName: {i.Name} \nCredit: {i.credit}\n---")


def input_marks(students, courses):
    if not courses or not students:
        print("Both students and courses must exist before entering marks.")
        return

    print("\n--- Select Course ---")
    list_cour(courses)
    course_id = int(input("Enter Course ID to input marks for: "))

    course_exists = any(c.id == course_id for c in courses)
    if not course_exists:
        print("Invalid Course ID.")
        return

    for student in students:
        mark = float(input(f"Enter mark for {student.Name} (ID: {student.id}): "))
        x = m.floor(mark * 10) / 10
        marks[(course_id, student.id)] = x
    print("Marks entered successfully!")


# === HÀM TÍNH VÀ HIỂN THỊ GPA ĐÃ ĐƯỢC SỬA ===
def calculate_and_show_gpa(students, courses):
    if not students or not courses:
        print("Need both students and courses to calculate GPA.")
        return

    # Map course_id -> credit để tra cứu nhanh
    course_credits = {c.id: c.credit for c in courses}

    for student in students:
        stu_marks = []
        stu_credits = []

        # Lấy tất cả các điểm và tín chỉ tương ứng của sinh viên này
        for course in courses:
            if (course.id, student.id) in marks:
                stu_marks.append(marks[(course.id, student.id)])
                stu_credits.append(course_credits[course.id])

        if stu_marks and sum(stu_credits) > 0:
            marks_array = np.array(stu_marks)
            credits_array = np.array(stu_credits)
            # Tính Weighted Average bằng NumPy
            gpa = np.average(marks_array, weights=credits_array)
            student.gpa = m.floor(gpa * 100) / 100  # Làm tròn 2 chữ số thập phân
        else:
            student.gpa = 0.0

    # Sắp xếp danh sách sinh viên theo GPA giảm dần
    students.sort(key=lambda s: s.gpa, reverse=True)

    print("\n=== GPA RANKING (Descending) ===")
    for s in students:
        print(f"ID: {s.id} | Name: {s.Name} | GPA: {s.gpa:.2f}")


def show_marks(students, courses):
    if not courses:
        print("No courses available.")
        return

    print("\n--- Select Course ---")
    list_cour(courses)
    course_id = int(input("Enter Course ID to view marks: "))

    course = next((c for c in courses if c.id == course_id), None)
    if not course:
        print("Invalid Course ID.")
        return

    print(f"\n--- Marks for Course: {course.Name} (ID: {course_id}) ---")
    found_any = False
    for student in students:
        if (course_id, student.id) in marks:
            found_any = True
            print(f"Student: {student.Name} (ID: {student.id}) -> Mark: {marks[(course_id, student.id)]}")

    if not found_any:
        print("No marks recorded yet for this course.")


def main():
    students = list()
    courses = list()
    exit_flag = False
    while not exit_flag:
        print("\nCourse and Student management: ")
        print("[1]: List Course(s)")
        print("[2]: List Student(s)")
        print("[3]: Add student info")
        print("[4]: Add course info")
        print("[5]: Input marks for a course")
        print("[6]: Show student marks for a course")
        print("[7]: Show GPA & Ranking")
        print("[q]: Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_cour(courses)
        elif choice == "2":
            list_stu(students)
        elif choice == "3":
            students.append(add_student_info())
        elif choice == "4":
            courses.append(add_course_info())
        elif choice == "5":
            input_marks(students, courses)
        elif choice == "6":
            show_marks(students, courses)
        elif choice == "7":
            calculate_and_show_gpa(students, courses)
        elif choice.lower() == "q":
            exit_flag = True


if __name__ == "__main__":
    main()