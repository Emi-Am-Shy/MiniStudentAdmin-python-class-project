import csv
from datetime import date

# ==========================================
# Task 2: LinkedQueue ADT (Waitlist)
# ==========================================
class Node:
    """This is the initiation of a wrapper for the data"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    """FIFO Queue implemented using a Linked List (No Python lists allowed)"""
    #Contains the logic by which the nodes are implemented into a list
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        """Adds an item to the back of the queue."""
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if self.is_empty():
            raise ValueError("Queue is empty: Cannot dequeue.")
        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return data

    def is_empty(self):
        """Returns True if the queue has no elements."""
        return self._size == 0

    def __len__(self):
        return self._size

# ==========================================
# Algorithms: Sorting and Searching
# ==========================================
def selection_sort(arr, key_func):
    """O(n^2) - Sorts the roster by a specific key."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key_func(arr[j]) < key_func(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def recursive_binary_search(arr, target_id, left, right):
    """O(log n) - Recursively locates a student by ID."""
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid].student.student_id == target_id:
        return mid
    elif target_id < arr[mid].student.student_id:
        return recursive_binary_search(arr, target_id, left, mid - 1)
    else:
        return recursive_binary_search(arr, target_id, mid + 1, right)


# Core Management Classes

class EnrollmentRecord:
    """Wraps a student object with a timestamp for registration tracking."""
    def __init__(self, student, enroll_date=None):
        self.student = student
        self.enroll_date = enroll_date if enroll_date else date.today().isoformat()

class Course:
    """Represents a University course with capacity and waitlist management."""
    def __init__(self, course_code, credits, capacity=30):
        self.course_code = course_code
        self.credits = int(credits)
        self.capacity = int(capacity)
        self.enrolled_roster = []
        self.waitlist = LinkedQueue()
        self._is_sorted_by_id = False

    def add_student(self, student_obj):
        """Enrolls a student or adds them to the waitlist if the course is full."""
        record = EnrollmentRecord(student_obj)
        if len(self.enrolled_roster) < self.capacity:
            self.enrolled_roster.append(record)
            self._is_sorted_by_id = False
            return "Enrolled"
        else:
            self.waitlist.enqueue(record)
            return "Waitlisted"

    def drop_student(self, student_id):
        """Removes a student using Binary Search and pulls from the waitlist."""
        if not self._is_sorted_by_id:
            selection_sort(self.enrolled_roster, lambda x: x.student.student_id)
            self._is_sorted_by_id = True
        
        idx = recursive_binary_search(self.enrolled_roster, student_id, 0, len(self.enrolled_roster)-1)
        
        if idx is not None:
            self.enrolled_roster.pop(idx)
            if not self.waitlist.is_empty():
                next_record = self.waitlist.dequeue()
                self.enrolled_roster.append(next_record)
                self._is_sorted_by_id = False
            return True
        return False

class Student:
    """Represents a student and tracks their academic progress."""
    GRADE_POINTS = {'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D':1.0, 'F':0.0}

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {} # Course Obj -> Grade String

    def enroll(self, course_obj, grade="In Progress"):
        """Attempts to enroll the student in a specific course object."""
        status = course_obj.add_student(self)
        if status == "Enrolled":
            self.courses[course_obj] = grade
        return status


# Task 3: Data Loading & Main Execution
class University:
    """High-level manager to coordinate students and courses."""
    def __init__(self):
        self.students = {}
        self.courses = {}

    def load_from_csv(self, file_path):
        """Parses the university data file and populates the system."""
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                s_id, s_name = row['student_id'], row['name']
                student = self.students.setdefault(s_id, Student(s_id, s_name))
                
                if row['courses']:
                    for item in row['courses'].strip(';').split(';'):
                        if ':' in item:
                            code, grade = item.split(':')
                            course = self.courses.setdefault(code, Course(code, 3))
                            student.courses[course] = grade

if __name__ == "__main__":
    u = University()
    # Replace 'university_data.csv' with your actual filename
    # u.load_from_csv('university_data.csv')
    print("University System Initialized.")