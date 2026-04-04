import csv
from datetime import date

# Task 1: EnrollmentRecord
class EnrollmentRecord:
    """Wraps a student object with a timestamp for registration tracking."""
    def __init__(self, student, enroll_date=None):
        self.student = student
        # Stores date as YYYY-MM-DD string
        self.enroll_date = enroll_date if enroll_date else date.today().isoformat()

# Task 2: LinkedQueue ADT (Waitlist)
class Node:
    """The basic building block for the LinkedQueue."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    """FIFO Queue implemented using a Linked List (No Python lists allowed)."""
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        """Adds an item to the back of the queue (O(1))."""
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Removes and returns the item from the front of the queue (O(1))."""
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

# Algorithms: Task 4 (Sorting) & Task 5 (Searching)
def selection_sort(arr, key_func):
    """O(n^2) algorithm to sort the roster."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key_func(arr[j]) < key_func(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr, key_func):
    """O(n^2) algorithm - Second required sorting algorithm."""
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_func(key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def recursive_binary_search(arr, target_id, left, right):
    """O(log n) - Recursively locates an EnrollmentRecord by student_id."""
    if left > right:
        return None
    mid = (left + right) // 2
    # Accessing the student_id through the EnrollmentRecord wrapper
    current_id = arr[mid].student.student_id
    if current_id == target_id:
        return mid
    elif target_id < current_id:
        return recursive_binary_search(arr, target_id, left, mid - 1)
    else:
        return recursive_binary_search(arr, target_id, mid + 1, right)

# Task 3: Course Capacity & Logic
class Course:
    """Represents a Course with capacity and waitlist management."""
    def __init__(self, course_code, credits, capacity=30):
        self.course_code = course_code
        self.credits = int(credits)
        self.capacity = int(capacity)
        self.enrolled_roster = []      # List of EnrollmentRecords
        self.waitlist = LinkedQueue()  # LinkedQueue of EnrollmentRecords
        self.enrolled_sorted_by = None # Tracks current sort state

    def add_student(self, student_obj, enroll_date=None):
        """Task 3: Enrolls student or adds to waitlist if full."""
        # Check if already enrolled (Task 3 requirement)
        for record in self.enrolled_roster:
            if record.student.student_id == student_obj.student_id:
                return "Already Enrolled"

        new_record = EnrollmentRecord(student_obj, enroll_date)
        
        if len(self.enrolled_roster) < self.capacity:
            self.enrolled_roster.append(new_record)
            self.enrolled_sorted_by = None # Order is now disturbed
            return "Enrolled"
        else:
            self.waitlist.enqueue(new_record)
            return "Waitlisted"

    def sort_enrolled(self, by='id', algorithm='selection'):
        """Task 4: Sorts roster by 'name', 'id', or 'date'."""
        # Define the key extraction logic
        if by == 'name':
            key_func = lambda x: x.student.name
        elif by == 'date':
            key_func = lambda x: x.enroll_date
        else: # Default to ID
            key_func = lambda x: x.student.student_id
        
        # Choose the algorithm
        if algorithm == 'insertion':
            insertion_sort(self.enrolled_roster, key_func)
        else:
            selection_sort(self.enrolled_roster, key_func)
        
        self.enrolled_sorted_by = by

    def drop_student(self, student_id):
        """Task 3 & 5: Uses Binary Search to drop and pulls from waitlist."""
        # Requirement: Must use Binary Search if sorted by ID
        if self.enrolled_sorted_by != 'id':
            self.sort_enrolled(by='id', algorithm='selection')
        
        idx = recursive_binary_search(self.enrolled_roster, student_id, 0, len(self.enrolled_roster)-1)
        
        if idx is not None:
            self.enrolled_roster.pop(idx)
            
            # Auto-enroll from waitlist (Task 3)
            if not self.waitlist.is_empty():
                next_student_record = self.waitlist.dequeue()
                # Update enrollment date to today for the new student
                next_student_record.enroll_date = date.today().isoformat()
                self.enrolled_roster.append(next_student_record)
                self.enrolled_sorted_by = None # Order disturbed by new addition
            return True
        return False

# Supporting Classes
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {} # Course Obj -> Grade

    def enroll(self, course_obj):
        status = course_obj.add_student(self)
        if status == "Enrolled":
            self.courses[course_obj] = "In Progress"
        return status

class University:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def load_from_csv(self, file_path):
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                s_id, s_name = row['student_id'], row['name']
                student = self.students.setdefault(s_id, Student(s_id, s_name))
                
                if row['courses']:
                    for item in row['courses'].strip(';').split(';'):
                        if ':' in item:
                            code, grade = item.split(':')
                            # Default capacity 30 as per task 6.3
                            course = self.courses.setdefault(code, Course(code, 3, 30))
                            student.courses[course] = grade

if __name__ == "__main__":
    u = University()
    print("University System Initialized (Milestone 2 Tasks 1-5 Complete). - Alex M")