# Enrollment Class has all the instances of students, classes and admins
# Handles transactions between its attributes
class Enrollment:

    def __init__(self):
        self.students = []
        self.classes = []
        self.admins = []

    def addCourse(self, admin): #Admin can initialize a course to be added
        print('  ____  ___    ___           __   ___   __ __  ____    _____   ___\n',
                ' /    ||   \  |   \         /  ] /   \ |  |  ||    \  / ___/  /  _]\n',
                '|  o  ||    \ |    \       /  / |     ||  |  ||  D  )(   \_  /  [_\n',
                '|     ||  D  ||  D  |     /  /  |  O  ||  |  ||    /  \__  ||    _]\n',
                '|  _  ||     ||     |    /   \_ |     ||  :  ||    \  /  \ ||   [_\n',
                '|  |  ||     ||     |    \     ||     ||     ||  .  \ \    ||     |\n',
                '|__|__||_____||_____|     \____| \___/  \__,_||__|\_|  \___||_____| \n')
        print("Course Name: ", end='')
        name = input()
        print("Course Code: ", end='')
        code = input()
        print("Course Units: ", end='')
        units = input()
        print("Course Professor: ", end='')
        professor = input()
        print("Days of the Week (M,T,W,H,F,S): ", end='')
        days = input()
        print("Time Span (Military Time) : ", end='')
        time = input()
        print("Section: ", end='')
        section = input()
        print("Course Number: ", end='')
        classNbr = input()
        print("Classroom: ", end='')
        room = input()
        print("Course Student Capacity: ", end='')
        maxCapacity = input()

        course = Course(name, code, (int)(units), professor, days, time, section, classNbr, room, (int)(maxCapacity))  # Initializes a course

        if admin.addCourse(self.classes, course):  # Adds course to the list of available courses
            print("Course Succesfully Added.")

    def removeCourse(self, admin): #Admin can remove a course from the list of courses in Enrollment
        print(' ____     ___  ___ ___   ___   __ __    ___         __   ___   __ __  ____    _____   ___ \n',
                '|    \   /  _]|   |   | /   \ |  |  |  /  _]       /  ] /   \ |  |  ||    \  / ___/  /  _]\n',
                '|  D  ) /  [_ | _   _ ||     ||  |  | /  [_       /  / |     ||  |  ||  D  )(   \_  /  [_ \n',
                '|    / |    _]|  \_/  ||  O  ||  |  ||    _]     /  /  |  O  ||  |  ||    /  \__  ||    _]\n',
                '|    \ |   [_ |   |   ||     ||  :  ||   [_     /   \_ |     ||  :  ||    \  /  \ ||   [_ \n',
                '|  .  \|     ||   |   ||     | \   / |     |    \     ||     ||     ||  .  \ \    ||     |\n',
                '|__|\_||_____||___|___| \___/   \_/  |_____|     \____| \___/  \__,_||__|\_|  \___||_____|\n')
        self.displayCourses()
        print("Enter Class Number of Class to be Removed: ")
        nbr = input()
        for c in self.classes:
            if nbr == c.classNbr:
                course = c
                admin.removeCourse(self.classes, course, self)
                return

        print("Course not found.")  # If loop terminated without finding class with input as class number

    def displayCourses(self):  # Will display list of courses and the information for each course
        print('  ______   ______   __  __   ______   ______   ______       __       __   ______   ______  \n',
                '/\  ___\ /\  __ \ /\ \/\ \ /\  == \ /\  ___\ /\  ___\     /\ \     /\ \ /\  ___\ /\__  _\ \n',
                '\ \ \____\ \ \/\ \\\\ \ \_\ \\\\ \  __< \ \___  \\\\ \  __\     \ \ \____\ \ \\\\ \___  \\\\/_/\ \/ \n',
                ' \ \_____\\\\ \_____\\\\ \_____\\\\ \_\ \_\\\\/\_____\\\\ \_____\    \ \_____\\\\ \_\\\\/\_____\  \ \_\ \n',
                '  \/_____/ \/_____/ \/_____/ \/_/ /_/ \/_____/ \/_____/     \/_____/ \/_/ \/_____/   \/_/ \n')

        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")
        print("{0:20} {1:20} {2:20} {3:20} {4:20} {5:20} {6:20} {7:20} {8:<20}".format("CLASSNBR", "COURSE", "SECTION", "DAYS", "TIME", "ROOM", "ENRL CAP", "ENROLLED", "PREREQ"))
        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")
        for i in range(len(self.classes)):
            prereqs = ''
            for j in range(len(self.classes[i].prereqs)):  # Will append all prerequisites of a subject in one line
                prereqs = prereqs + self.classes[i].prereqs[j].code
            print("{0:<20} {1:20} {2:20} {3:20} {4:20} {5:20} {6:<20} {7:<20} {8:<20}".format(self.classes[i].classNbr,
                                                                                              self.classes[i].name,self.classes[i].section,
                                                                                              self.classes[i].days,self.classes[i].time,
                                                                                              self.classes[i].room,self.classes[i].maxCapacity,
                                                                                              len(self.classes[i].students), prereqs))
        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")

    def addStudent(self):  # A method instance of addstudent where Admin will define the student to be added to Enrollment
        print('  ____  ___    ___         _____ ______  __ __  ___      ___  ____   ______ \n',
                ' /    ||   \  |   \       / ___/|      ||  |  ||   \    /  _]|    \ |      |\n',
                '|  o  ||    \ |    \     (   \_ |      ||  |  ||    \  /  [_ |  _  ||      |\n',
                '|     ||  D  ||  D  |     \__  ||_|  |_||  |  ||  D  ||    _]|  |  ||_|  |_|\n',
                '|  _  ||     ||     |     /  \ |  |  |  |  :  ||     ||   [_ |  |  |  |  |  \n',
                '|  |  ||     ||     |     \    |  |  |  |     ||     ||     ||  |  |  |  |  \n',
                '|__|__||_____||_____|      \___|  |__|   \__,_||_____||_____||__|__|  |__|  \n')
        print("Student's Full Name: ", end='')
        name = input()
        print("Student's username: ", end='')
        username = input()
        print("Student's password: ", end='')
        password = input()
        print("Student's age: ", end='')
        age = input()
        print("Student's degree program: ", end='')
        program = input()
        print("Student's college: ", end='')
        college = input()

        self.students.append(Student(username, password, name, age, program, college))

    def initAddStudent(self, student):
        self.students.append(student)

    def initAddAdmin(self, admin):
        self.admins.append(admin)


# This class defines a Course and its attributes
class Course:
    def __init__(self, name, code, units, professor, days, time, section, classNbr, room, maxCapacity):
        self.name = name
        self.code = code
        self.units = units
        self.professor = professor
        self.days = days
        self.time = time
        self.section = section
        self.classNbr = classNbr
        self.room = room
        self.maxCapacity = maxCapacity

        self.students = []
        self.prereqs = []

    def addStudent(self, student):  # Adds a student to the course
        if len(self.students) < self.maxCapacity and self.validate(student):  # If course is not yet full and stduent is valid to enroll.
            self.students.append(student)
            return True  # For validation.
        else:
            print('You cannot enroll.')
            return False  # If the system failed to enroll student to a course.

    def removeStudent(self, student):  # Removes a student from a course
        for elem in self.students:
            if elem == student:  # If student is in the enrolled students for the course
                self.students.remove(student)

    def addPrereq(self, prereq):
        self.prereqs.append(prereq)

    def validate(self, student):  # Checks if prerequisites are already computed
        for elem in self.prereqs:
            if elem not in student.completedcourses:
                return False  # Returns false if at least one prerequisite is not completed by the student.

        return True


# This class is for the student entity of the enrollment system containing its attributes
class Student:
    idNum = 1000  # Initial value for the Student ID Numbers, this will get incremented per student who registers

    def __init__(self, username, password, name, age, program, college):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.program = program
        self.idNum = Student.idNum
        Student.idNum += 1
        self.college = college
        self.courses = []
        self.completedcourses = []

    def addCompletedCourse(self, user, course):  # Adds a completed course to list of completed courses for the student
        if user is None:
            self.completedcourses.append(course)
            return
        if course not in self.courses:  # If student is not currently enrolled in the class chosen
            print("You cannot add this to your completed courses.")
            return
        if course in self.completedcourses:  # If course chosen is already completed
            print("You have already completed this course.")
            return
        print("You have successfully added course to completed courses.")
        self.completedcourses.append(course)  # Add to completed courses, if valid course
        self.courses.remove(course)  # Remove course from list of courses currently being taken
        course.removeStudent(self)  # Remove student from list of students in the course

    def addCourse(self, course):  # Adds a course to list of courses student in currently taking
        if course in self.courses:  # If student is already taking the course
            print("You already have that class in your EAF.")
            return

        if course in self.completedcourses:  # If course is already completed by the student
            print("You have already completed this course.")
            return

        if course.addStudent(self):  # If course is added successfully from the return value of the addStudent
            print("Course added successfully.")
            self.courses.append(course)
        else:  # If student was not enrolled due to invalidity.
            print("Failed to add course. Requirements are not fulfilled to be eligible to enroll.")
            return

    def removeCourse(self, course):  # This will allow student to drop courses
        for elem in self.courses:
            if course == elem:
                self.courses.remove(elem)
                course.removeStudent(self)
                print("Course removed successfully.")
                return

        # If student is not currently taking the course chosen

        print("Error: You do not have a course named", course.name, " in your list.")

    def display(self):  # This will display all the Information about the student
        print('  _____ ______  __ __  ___      ___  ____   ______      ____  ____   _____   ___  \n',
                ' / ___/|      ||  |  ||   \    /  _]|    \ |      |    |    ||    \ |     | /   \ \n',
                '(   \_ |      ||  |  ||    \  /  [_ |  _  ||      |     |  | |  _  ||   __||     |\n',
                ' \__  ||_|  |_||  |  ||  D  ||    _]|  |  ||_|  |_|     |  | |  |  ||  |_  |  O  |\n',
                ' /  \ |  |  |  |  :  ||     ||   [_ |  |  |  |  |       |  | |  |  ||   _] |     |\n',
                ' \    |  |  |  |     ||     ||     ||  |  |  |  |       |  | |  |  ||  |   |     |\n',
                '  \___|  |__|   \__,_||_____||_____||__|__|  |__|      |____||__|__||__|    \___/ \n')
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Program: ", self.program)
        print("College: ", self.college)
        print("ID Number: ", self.idNum)
        print("\noOo------------------------------Courses-------------------------------oOo ")
        self.displayCourses(self.courses)
        print("\n\noOo-------------------------CompletedCourses---------------------------oOo")
        self.displayCourses(self.completedcourses)

    def displayCourses(self, courses):  # This will display all the courses being taken by the student
        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")
        print("{0:20} {1:20} {2:20} {3:20} {4:20} {5:20} {6:20} {7:20}".format("CLASSNBR", "COURSE", "SECTION", "DAYS", "TIME", "ROOM", "ENRL CAP", "ENROLLED"))
        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")
        for elem in courses:
            print("{0:<20} {1:20} {2:20} {3:20} {4:20} {5:20} {6:<20} {7:<20}".format(elem.classNbr, elem.name, elem.section, elem.days, elem.time, elem.room, elem.maxCapacity, len(elem.students)))
        print("@}}>---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------{---(@")


# This class defines an admin and its attributes
class Admin:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def addCourse(self, courses, course):  # This allows an admin to add a course to the Enrollment System
        for elem in courses:
            if course.classNbr == elem.classNbr:  # If course class number is already in the system
                print("Course Number already exists")
                return False

        # If course is valid to be added to the system
        courses.append(course)
        return True

    def removeCourse(self, courses, course, enrollment):  # Removes a course from the system
        if course in courses:  # If course is in the system (It can be removed)
            courses.remove(course)  # Remove course from the system
            for student in enrollment.students:  # Remove course from all students who are taking the course
                if course in student.courses:
                    student.courses.remove(course)

            print("Successfuly removed.")
            return
        else:
            print("Course not in lists.")


# Initializations

trisha = Student("trisha", "isthebest", "Trisha Pelagio", 19, "BSCS-ST", "College Of Computer Studies")
bryce = Student("bryce", "hehe", "Bryce Ramirez", 19, "BSCS-ST", "College Of Computer Studies")
rey = Student("rey", "lol", "Rey Delima", 20, "BSCS-NE", "CCS")
marc = Student("marc", "dancer", "Marc Gonzales", 20, "BSCS-CSE", "College Of Computer Studies")

comet = Course("COMET", "CMT", 3, "Elsa Snow", "TH", "11:00-12:30", "S16", "1002", "G302B", 3)
csmath2 = Course("Algebra", "CSMATH2", 4, "Duke Delos Santo", "WF", "0915-1045", "S11", "2001", "G204", 3)
csmath2.addPrereq(comet)
gefili1 = Course("Filipino", "GEFILI1", 3, "Lilibeth Quiore", "TH", "0730-0900", "S11", "2002", "G206", 4)
gefili1.addPrereq(comet)
ccprog3 = Course("OOP", "CCPROG3", 3, "Shirley Chu", "WF", "0730-0900", "S16", "2003", "G302B", 3)


elsa = Admin("queen", "elsa", "Elsa Frost")
x = Enrollment()
x.initAddAdmin(elsa)
elsa.addCourse(x.classes, comet)
elsa.addCourse(x.classes, csmath2)
elsa.addCourse(x.classes, gefili1)
elsa.addCourse(x.classes, ccprog3)

x.initAddStudent(rey)
x.initAddStudent(marc)
x.initAddStudent(trisha)
x.initAddStudent(bryce)
trisha.addCompletedCourse(user=None, course=comet)


# Main Program

# Only the admin can add new student users

#          STUDENT USERS
# username : trisha  | password: isthebest
# username : bryce  | password: hehe
# username : rey  | password: lol
# username : marc  | password: dancer

#          ADMIN USERS
# username : queen  | password: elsa


while True:
    user = 0
    while user == 0:
        print("                         ooooooooo   ooooo        oooooooo8  ooooo  oooo                          ")
        print("                          888    88o  888        888          888    88                           ")
        print("                          888    888  888         888oooooo   888    88                           ")
        print("                          888    888  888      o         888  888    88                           ")
        print("                         o888ooo88   o888ooooo88 o88oooo888    888oo88                            ")
        print("                                                                                                  ")
        print("     o                   o88                                  oooooooooo                          ")
        print("    888     oo oooooo    oooo  oo ooo oooo     ooooooo         888    888 oo oooooo     ooooooo   ")
        print("   8  88     888   888    888   888 888 888  888     888       888oooo88   888    888 888     888 ")
        print("  8oooo88    888   888    888   888 888 888  888     888       888    888  888        888     888 ")
        print("o88o  o888o o888o o888o  o888o o888o888o888o   88ooo88        o888ooo888  o888o         88ooo88   \n")
        print("Username 👋≧◉ᴥ◉≦ : ", end='')
        username = input()

        for elem in x.students:
            if username == elem.username:
                user = elem
                break
        for elem in x.admins:
            if username == elem.username:
                user = elem
                break

        if user == 0:
            print("There are no users with that username.")

    passbool = False

    while not passbool:
        print("Password (ɔ◔‿◔)ɔ ♥ : ", end='')
        password = input()
        if password == user.password:
            print("Login Successful.")
            passbool = True
        else:
            print("Wrong password.")

    if type(user) == Student:
        feature = 0
        while feature != 6:
            print("\n\n\nʕ•́ᴥ•̀ʔっ ----------Welcome to the Student Enrollment System---------- ʕ•́ᴥ•̀ʔっ\n")
            print("Choose a feature (✿◠‿◠) : ")
            print("[1] Enrollment: Add Classes\n[2] Enrollment: Remove Classes\n[3] View Student Data\n[4] Add Completed Courses\n[5] Change Password\n[6] Sign out")
            feature = int(input())

            if feature == 1:
                print("List of available courses: \n")
                x.displayCourses()
                print("Enter Course Class Number to add ᕙ(^▿^-ᕙ): ", end='')
                course = 0
                classnum = input()
                for elem in x.classes:
                    if (elem.classNbr == classnum):
                        course = elem
                if course!= 0:
                    user.addCourse(course)
                else:
                    print("Invalid input. Try again.")

            elif feature == 2:
                print("Courses Added: ")
                user.displayCourses(user.courses)
                print("Enter Course Class Number to remove (╥﹏╥): ", end='')
                course = 0
                classnum = input()
                for elem in user.courses:
                    if (elem.classNbr == classnum):
                        course = elem
                if course != 0:
                    user.removeCourse(course)
                else:
                    print("Invalid input. Try again.")

            elif feature == 3:
                print('\n')
                user.display()
                print("Press Enter to Proceed ಥ_ಥ: ")

            elif feature == 4:
                user.displayCourses(user.courses)
                print("Enter Course Class Number to add (≖_≖ ):", end='')
                inp = input()
                course = 0
                for elem in user.courses:
                    if elem.classNbr == inp:
                        course = elem
                if course != 0:
                    user.addCompletedCourse(user, course)
                else:
                    print("Invalid Input")

            elif feature == 5:
                print("Current Username: ", user.username)
                print("Current Password: ", user.password)
                print("\nEnter New Password  (•◡•) /:", end='')
                password = input()
                user.password = password
                print("\nPassword Changed Successfully.")
            elif feature == 6:
                print("Thank you for using Animo Bro. You will now be logged out. \n\n\n")
            else:
                print("Invalid Input.(ง︡'-'︠)ง")
    else:
        feature = 0
        while(feature != 6):
            print("\n\n\nʕ•́ᴥ•̀ʔっ ----------Welcome to the Admin Enrollment System---------- ʕ•́ᴥ•̀ʔっ\n")
            print("Choose a feature (✿◠‿◠) :")
            print("[1] Add Courses\n[2] Remove Courses\n[3] Change Password\n[4] Add Student\n[5] View Courses\n[6] Sign Out")
            feature = int(input())
            if feature == 1:
                x.addCourse(user)
            elif feature == 2:
                x.removeCourse(user)
            elif feature == 3:
                print("Current Username: ", user.username)
                print("Current Password: ", user.password)
                print("\nEnter New Password ≧◠ᴥ◠≦✊:", end='')
                password = input()
                user.password = password
            elif feature == 4:
                x.addStudent()
            elif feature == 5:
                x.displayCourses()
            elif feature == 6:
                print("Thank you for using Animo Bro. You will now be logged out. (ɔ◔‿◔)ɔ ♥\n\n\n")
            else:
                print("Invalid Input. (ง︡'-'︠)ง")

