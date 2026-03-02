"""Hai Shiya! I'm like super sleepy yet so energized right now but I wanted 
to say I love you platonically and I appreciate you as my lab partner :3
"""

"""
Task 1: Implement the Course Class

A Course represents a single course in the university catalog (e.g., CSE2050).
Required Fields

• course code (string) — unique identifier for the course (e.g., "CSE1010").
• credits (integer ) — number of credits earned for completing the course.
• students (list of Student objects) — all students enrolled in the course.

Required Methods
• add student(student) — adds a Student object to the course roster.
• get student count() — returns the number of students currently enrolled.

Design note: The course is responsible for maintaining its own roster. A student enrolling in a course should
cause both the student and the course to reflect that relationship. The students list should mandatorily be
an object of Student class.
""" 

#Task 1 Begins Here
class Course: 
    """This Class represents a singl ecourse""" # Holds and maintains its own roster
    
    def __init__(self, course_code:str, credits:int, students = None):
        """Initializes a Course Roster with course_code, credits, and students"""
        self.course_code = course_code          # Identifyer: (string) The course CSE2050
        self.credits = credits                  # Identifyer: (integer) Number of credits earned for a completed course
        self.students = students                # Identifyer: (list of Student objects) All students enrolled in a course
        self.studentCount = 0

        if self.students == None:
            self.students = list([])
        pass
    
    def add_students(self):                # Purpose: Adds a Student(object) to the course roster
        self.students.append(self.students)
        self.studentCount += 1             # Purpose: Increases student count to a Course's roster
        return None

    def get_student_count(self):           # Purpose: Returns number of student currently enrolled
        return self.studentCount


"""
Task 2: Implement the Student Class

A Student represents an individual student and the set of courses they have taken (with grades).
Required Fields
• student id (string ) — unique identifier for the student.
• name (string) — the student’s name.
• courses (dictionary) — a dictionary of the courses a student has takes :
Course object : grade
where grade is a letter grade such as "A", "B+", etc.

Required Methods
• enroll(course, grade) — enrolls the student in a course with the given grade and updates the course
roster.
• update grade(course, grade) — modify the student grade for a particular course
• calculate gpa() — computes and returns the GPA using all graded courses and their credits.
• get courses() — returns a list of course objects taken by the student.
• get course info() — returns a structured summary of all enrollments, including course code, grade,
and credits.
2

Implementation guidance:
• Use the following letter-grade to grade-point mapping when computing GPA:
GRADE_POINTS = {
'A' : 4.0, 'A-' : 3.7,
'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
'D' : 1.0,
'F' : 0.0
}
• GPA must be weighted by course credits:
GPA =
P(grade points x credits)
Pcredits
"""
#Task 2 Begins Here

class Student:
    """Student represents an individual student and the SET of courses they have taken (with grades)"""
    
    GRADE_POINTS = {
    'A' : 4.0, 'A-' : 3.7,
    'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
    'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
    'D' : 1.0,
    'F' : 0.0
    }

    def __init__(self, student_id:str, name:str, course:None):
        self.student_id = student_id    # (string ) - unique identifier for the student.
        self.name = name                # (String) - The student’s name.
        self.course = course            # (Dict) - of the courses a student has taken, with grade
        
        if self.course == None:         # Sets the default parameter if Course input dict is empty
            course = {}

    def enroll(self, course, grade):
        """enrolls the student in a course with the given grade and updates the course roster."""
        self.course = course
        self.grade = grade

    def upgrade_grade(self):
        """modify the student grade for a particular course"""
        pass

    def calc_gpa(self): # Calculates GPA
        """computes and returns the GPA using all graded courses and their credits."""
        pass

    def get_courses(self): #Returns a list of course objects
        """returns a list of course objects taken by the student"""
        pass

    def get_course_info(self): #
        """returns the number of students currently enrolled"""
        pass

"""
Task 3: Implement the University Class

The University class serves as the central manager. It stores all students and courses and provides methods
to query enrollment information efficiently.

Required Fields
• students (dictionary) — maps student id → Student object.
• courses (dictionary) — maps course code → Course object.

Required Methods
• add course(course code, credits) — if the course does not exist, create and store it; return the
course object.
• add student(student id, name) — if the student does not exist, create and store them; return the
student object.
• get student(student id) — returns the student object for that ID (or None if not found).
• get course(course code) — returns the course object for that code (or None if not found).
• get course enrollment(course code) — returns the number of students enrolled in the given course.
• get students in course(course code) — returns a list of student objects enrolled in the given
course.

Design note: The dictionaries in University are meant to make lookup fast and simple. Use them to avoid
repeatedly scanning lists to find a student or course.
"""

#Task 3 Begins Here