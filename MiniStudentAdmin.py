"""Hai Shiya! I'm like super sleepy yet so energized right now but I wanted 
to say I love you platonically and I appreciate you as my lab partner :3 IM SORRY :( YOURE BULLYING ME
"""
import pandas as pd

# Load the catalog for credit lookups
df_catalog = pd.read_csv('course_catelog(in).cvs')
CREDIT_LOOKUP = dict(zip(df_catalog['course_code'], df_catalog['credits']))

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
    """This Class represents a single course""" # Holds and maintains its own roster
    
    def __init__(self, course_code: str, credits: int): #Students Removeed
        """Initializes a Course Roster with course_code, credits, and students"""
        self.course_code = course_code          
        self.credits = credits                  
        self.students = []  # Initialize as an empty regular list
        self.studentCount = 0
    
    def add_students(self, new_student):
        # Prevent adding the same student twice
        if new_student not in self.students:
            self.students.append(new_student)
            self.studentCount += 1

    def get_student_count(self):
        """Returns number of students currently enrolled"""
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
    GRADE_POINTS = {
        'A' : 4.0, 'A-' : 3.7, 'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
        'C+': 2.3, 'C' : 2.0, 'C-' : 1.7, 'D' : 1.0, 'F' : 0.0
    }

    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.courses_takendict = {} # Course Object : Letter Grade

    def enroll(self, new_course, grade): 
        """Enrolls student in course and updates the course's own roster."""
        self.courses_takendict[new_course] = grade
        # IMPORTANT: This tells the Course object to add this Student to its list!
        new_course.add_students(self)

    def upgrade_grade(self, course_obj, grade: str):
        if course_obj not in self.courses_takendict:
            raise RuntimeError("Student has not taken this course.")
        if grade not in self.GRADE_POINTS:
            raise ValueError("Letter grade DNE.")
        self.courses_takendict[course_obj] = grade

    def calc_gpa(self):
        total_quality_points = 0.0
        total_credits = 0
        
        # We iterate through the dictionary: the key is a Course Object
        for course_obj, letter_grade in self.courses_takendict.items():
            # 1. Get points from our class dictionary
            points = self.GRADE_POINTS.get(letter_grade, 0.0)
            
            # 2. Get credits directly from the Course object
            credits = course_obj.credits
            
            total_quality_points += (points * credits)
            total_credits += credits

        if total_credits == 0:
            return 0.0
            
        return round(total_quality_points / total_credits, 2)

    def get_courses(self):
        # Returns the Course objects (the keys of our dictionary)
        return list(self.courses_takendict.keys())

    def get_course_info(self):
        """Returns a summary of all enrollments."""
        summary = []
        for course_obj, grade in self.courses_takendict.items():
            info = f"{course_obj.course_code}: {grade} ({course_obj.credits} credits)"
            summary.append(info)
        return "\n".join(summary)
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

#Task 3 Begins 

class University:
    
    def __init__(self): #dictionaries in University are meant to lookup fast and simple
        self.students = {} # Maps student_id (str) -> Student Object
        self.courses = {} # Maps course_code (str) -> Course Object
    
    def add_course(self, course_code, credits): #if the student does not exist, create and store them; return the student object.
        if course_code not in self.courses:
            # Create a new Course object and store it
            self.courses[course_code] = Course(course_code, credits)
            
        return self.courses[course_code]

    def add_student(self, student_id, name): #if the student does not exist, create and store them; return the student object.
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            
        return self.students[student_id]

    def get_student(self, student_id): #returns the student object for that ID (or None if not found).
        return self.students.get(student_id)

    def get_course(self, course_code): #returns the course object for that code (or None if not found).
        return self.courses.get(course_code) 

    def get_course_enrollment(self, course_code): #returns the number of students enrolled in the given course.
        course = self.get_course(course_code)
        if course is None:
            return 0
        return len(course.students)
    
    def get_students_in_course(self, course_code): # returns a list of student objects enrolled in the given course.
        course = self.get_course(course_code)
        if course is None:
            return []
        return list(course.students)