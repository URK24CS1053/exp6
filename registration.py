class CourseRegistrationSystem:
    def __init__(self):
        self.courses = {
            "Math 101": 10,
            "Physics 101": 15,
            "Chemistry 101": 12,
            "Biology 101": 8
        }
        self.students = {}

    def display_courses(self):
        print("\nAvailable Courses:")
        for course, seats in self.courses.items():
            print(f"{course} - Seats Available: {seats}")

    def enroll(self, student_name, course_name):
        if course_name not in self.courses:
            print("This course does not exist.")
            return

        if self.courses[course_name] > 0:
            if student_name not in self.students:
                self.students[student_name] = []
            self.students[student_name].append(course_name)
            self.courses[course_name] -= 1
            print(f"{student_name} successfully enrolled in {course_name}.")
        else:
            print(f"Sorry, {course_name} is full.")

    def view_enrollment(self, student_name):
        if student_name in self.students:
            print(f"\n{student_name} is enrolled in the following courses:")
            for course in self.students[student_name]:
                print(course)
        else:
            print(f"{student_name} is not enrolled in any courses.")


system = CourseRegistrationSystem()


while True:
    print("\nMenu:")
    print("1. Display available courses")
    print("2. Enroll in a course")
    print("3. View enrolled courses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        system.display_courses()

    elif choice == '2':
        student_name = input("Enter your name: ")
        course_name = input("Enter course name to enroll in: ")
        system.enroll(student_name, course_name)

    elif choice == '3':
        student_name = input("Enter your name to view enrolled courses: ")
        system.view_enrollment(student_name)

    elif choice == '4':
        print("Exiting the system.")
        break

