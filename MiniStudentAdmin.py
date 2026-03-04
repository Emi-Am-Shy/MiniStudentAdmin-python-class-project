"""Hai Shiya! I'm like super sleepy yet so energized right now but I wanted 
to say I love you platonically and I appreciate you as my lab partner :3 IM SORRY :( YOURE BULLYING ME
youre a goated lab partner :DD
"""
#Miles stone 1 of CSE2025 ,Mini Student Admin.
# Lab Participants:  Juan Alexander Morquecho Velazquez, Shiya Subbaiah
"""
Task 1: Implement the Course Class

A Course represents a single course in the university catalog (e.g., CSE2050).
Required Fields

• course code (string) — unique identifier for the course (e.g., "CSE1010").
• credits (integer ) — number of credits earned for completing the course.
• students (list of Student objects) — all students enrolled in the course.

Required Methods
• add_student(student) — adds a Student object to the course roster.
• get_student_count() — returns the number of students currently enrolled.

Design note: The course is responsible for maintaining its own roster. A student enrolling in a course should
cause both the student and the course to reflect that relationship. The students list should mandatorily be
an object of Student class.
""" 

#Task 1 Begins Here
import csv
"""
CSV Is a required portion of this progam. 
CSV is a built in python Module which is designed to (efficiently) read csv files.
"""
import statistics
"""
Import statistic is a built in python Module with predefined methods that help preform mathematical operations.
For example: 
            Instead of having to write average = sum(my_list) / len(my_list), 
            all I need to do is call statistics.mean(data)

Furthermore, this class has better reliability when dealing with floating point number
"Just like the ones a grading system would have"
"""

class Course:
    """This class creates objects that represents a single course in the university catalog (e.g., CSE2050) """
    
    """Designed by: Juan M. Velazquez, and Shiya Subbaiah"""
    def __init__(self, course_code, credits): #O(1) - Alex
        """This method initializes the Course Class's attributes, linking them to the object created by this class"""
        self.course_code = course_code # Instance Attributes Class: (string) - Unique identifier that defines the course (e.g., "CSE1010") 
        self.credits = int(credits)    # Instance Attributes Class: (integer) - Defines number of credits earned for completing the course
        self.students = []             # Instance Attributes Class: list("Of all student OBJECTS") - all students enrolled in the course

    def add_student(self, student_obj): #O(1)- Alex
        """Task 1: adds a Student object to the course roster."""
        if student_obj not in self.students: #This line is a secruity meassure
            """Case Prevention: Duplicates - it prevents duplicates by referencing the (student_object) 
                                             we're inserting(enrolling) with the function
                                             with student object already created (self.student)
                                             
                                             This line makes the program go into the memory of Student objects(self.student(s)) created
                                             and returns "True" if the "student_object" we're inserting is not in "self.student(s)"
                                                - This only adds the "student_object" to the list of Student Objects(self.student(s))
                                                  enrolled into the Course, if the object does not already exist
                                             """
            self.students.append(student_obj) # Enrolls student_object into the list of students enrolled 

    def get_student_count(self): #O(1) - Shiya
        """Task 1: returns the number of students currently enrolled."""
        return len(self.students) # Uses the list method len() which returns the count of students enrolled


"""
Task 2: Implement the Student Class

A Student represents an individual student and the set of courses they have taken (with grades).
Required Fields
• student_id (string) — unique identifier for the student.
• name (string) — the student’s name.
• courses (dictionary) — a dictionary of the courses a student has takes :
Course object : grade
where grade is a letter grade such as "A", "B+", etc.

Required Methods
• enroll(course, grade) — enrolls the student in a course with the given grade and updates the course
roster.
• update_grade(course, grade) — modify the student grade for a particular course
• calculate_gpa() — computes and returns the GPA using all graded courses and their credits.
• get_courses() — returns a list of course objects taken by the student.
• get_course info() — returns a structured summary of all enrollments, including course code, grade,
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
    """Student class represents an individual student and the set of courses they have taken (with grades). Required Fields"""
    
    """Designed by: Juan A Morquecho, and Shiya Subbaiah"""
    
    #This dictionary defines all letter grades(Represented by strings) as keys, 
    #with associated float point values(4.0, 4.1 etc) of grades 
    GRADE_POINTS = {                            
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0
    }

    def __init__(self, student_id, name): #O(1)- Shiya
        """
        This method inizializes the class attributes. 
        Student ID - Is an identifer for this specific "Student" 
        Name - Associates a particular name with the student's ID
        """
        
        """Student ID is always 8 characters long, and starts with STU. 
           
           With this information we can use it to create a case prevention measure 
           for when someone is creating a student object.  

           Case Prevention: Value errors - Invalid IDs, or Name
          
          """
        # Condition 1: If len of student_ID is not equal to 8 return True:  Run command
        # Condition 2: If student_id does not start with "STU" return True: Run Command
        #Condition 3: If name is only spaces return True

        # When both these conditions are true, the ID is allowed passed the first secruity check.
        if len(student_id) != 8 or not student_id.startswith("STU"): #Check is length of the string is 8 char long, 
                                                                     #The "or" opperator allows to have two, or more conditional statments be put on a single line

            raise ValueError(f"Invalid ID: {student_id}, does not start with STU, or is 8 characters long") #Intentional Crash
        
        # Checks if name is not just a space
        if not name.strip():  #.strip("character removed") is a built in python method for string             
                                                                        #this is needed since without it an our past security check doesn't protect the pogram from it
            raise ValueError("Name cannot be empty") #Inentional Crash
        
        self.student_id = student_id # Instance Attributes Class: (string) - Unique identifier that defines the student's ID (e.g., "STU00001") 
        self.name = name             # Instance Attributes Class: (string) - Unique identifier that defines the student's name (e.g., "Student_1")
        self.courses = {}            # Instance Attribute  Class: (Dictionary) - Courses student has taken(key), with the
                                                                               # grade that student earned for the course(val). 
                                                                               # self.courses = {CourseObj: grade_string}, default {}

    def enroll(self, course_obj, grade): #O(1)- Shiya
        """Task 2: enrolls the student and updates course roster."""
        """Since grade points  both as points and letters are already defined,
           we can just check to see if they're in the dictionary(GRADE_POINTS)"""
        
        if grade not in self.GRADE_POINTS: #Secruity check: Returns True if the input(grade), is not in dictionary, "self.GRADE_POINTS".
            raise ValueError(f"Invalid grade: {grade}")
        
        self.courses[course_obj] = grade #Once the tests are passed the course list of student's classes taken(Which is actually a dictionary), gets updated
        course_obj.add_student(self) 

    def update_grade(self, course_obj, grade): #O(1)- Alex
        """Task 2: modify the student grade for a particular course."""
        if course_obj in self.courses: # Secruity Check: This line makes sure to only edit courses already in the students own course list 
            self.courses[course_obj] = grade #If the course_object exists as a key in our dictionary, update the val of that dictionary

    def calculate_gpa(self): #O(n)- Alex
        """Task 2: Weighted GPA calculation."""
        total_qp = 0.0 # Total Quality Points: Represents the sum of (Grade Value * Course Credits)
        total_cr = 0 # Total Credits: Represents the sum of all credits taken

        for course, grade in self.courses.items(): # This for loop cycles through the range of items within the list of courses taken
                                                   # .items(), accesses (key:val) pairs from a dictionary 
            total_qp += (self.GRADE_POINTS[grade] * course.credits)  #The grade val(float) associated with the grade letter(string) * course credits
            total_cr += course.credits
        return round(total_qp / total_cr, 2) if total_cr > 0 else 0.0

    def get_courses(self): #O(1) - Alex
        """Task 2: returns a list of course objects taken."""
        return list(self.courses.keys())

    def get_course_info(self): #O(1)- Alex
        """Task 2: returns structured summary of all enrollments."""
        return [f"{c.course_code}: {g} ({c.credits}cr)" for c, g in self.courses.items()]
"""
Task 3: Implement the University Class

The University class serves as the central manager. It stores all students and courses and provides methods
to query enrollment information efficiently.

Required Fields
• students (dictionary) — maps student id → Student object.
• courses (dictionary) — maps course code → Course object.

Required Methods
• add_course(course code, credits) — if the course does not exist, create and store it; return the
course object.
• add_student(student id, name) — if the student does not exist, create and store them; return the
student object.
• get_student(student id) — returns the student object for that ID (or None if not found).
• get_course(course code) — returns the course object for that code (or None if not found).
• get_course_enrollment(course code) — returns the number of students enrolled in the given course.
• get_students_in_course(course code) — returns a list of student objects enrolled in the given
course.

Design note: The dictionaries in University are meant to make lookup fast and simple. Use them to avoid
repeatedly scanning lists to find a student or course.
"""

#Task 3 Begins 

class University:
    """It stores all students and courses and provides method to query enrollment information efficiently."""
    """Designed by: Alex Morquecho Velazquez, Shiya Subbaiah"""
    def __init__(self): #O(1)- Shiya
        """Initializes a University object with empty dictionaries to store students (by ID) and courses (by course code) """ 
        
        self.students = {} # ID -> Student Obj
        self.courses = {}  # Code -> Course Obj

    def add_course(self, code, credits): #O(1)- Shiya
        """" Creates and stores a new Course object if it does not already exist and returns the corresponding course object."""
        if code not in self.courses:
            self.courses[code] = Course(code, credits)
        return self.courses[code]

    def add_student(self, student_id, name): #O(1)- Shiya
        """Creates and stores a new Student object if it does not already exist and returns the corresponding student object. """
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        return self.students[student_id]

    def get_student(self, sid): #O(1)- Shiya
        """instantly retrieve a specific Student object from the university's records using their unique ID"""
        return self.students.get(sid)

    def get_course(self, code): #O(1)- Shiya
        """Instantly retrieves a specific Course object from the university's dictionary using its unique code."""
        return self.courses.get(code)

    def get_course_enrollment(self, code): #O(1)- Shiya
        """finds the specific course by its code and returns the total number of students currently on its roster"""
        course = self.get_course(code)
        return course.get_student_count() if course else 0

    def get_students_in_course(self, code): #O(1)- Shiya
        """retrieves the specific Course object using its unique code and returns its full list of enrolled Student"""
        course = self.get_course(code)
        return course.students if course else []
    
    # --- DEMONSTRATION METHODS ---

    def get_common_students(self, code1, code2): #O(1)- Alex
        """Returns intersection of students in two courses."""
        set1 = set(self.get_students_in_course(code1))
        set2 = set(self.get_students_in_course(code2))
        return list(set1.intersection(set2))

    def get_university_gpa_stats(self): #O(1)- Alex
        """Calculate mean and median GPA for the whole university."""
        gpas = [s.calculate_gpa() for s in self.students.values()]
        if not gpas: return 0, 0
        return round(statistics.mean(gpas), 2), round(statistics.median(gpas), 2)

def load_data(uni): #O(n)- Alex
    """These functions make use of the the csv method .DictReader which simplifies the text file into organized objects."""
    # Load Catalog
    with open('course_catalog(in).csv', mode='r') as f:
        #the DictReader uses the first row of your file (the headers) to create a dictionary for every subsequent row.
        reader = csv.DictReader(f)
        for row in reader:
            uni.add_course(row['course_code'], row['credits'])

    # Load Students
    with open('university_data(in).csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = uni.add_student(row['student_id'], row['name'])
            if row['courses']:
                entries = row['courses'].strip(';').split(';')
                for item in entries:
                    if ':' in item:
                        code, grade = item.split(':')
                        c_obj = uni.get_course(code)
                        if c_obj: student.enroll(c_obj, grade)

if __name__ == "__main__":
    uni = University()
    load_data(uni)
    print("Data Loaded Successfully.")