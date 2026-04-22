#--------------------------------------------------------------------
#All work below this is done by Alex (Juan A Morquecho Velazquez)
#--------------------------------------------------------------------

from datetime import date

# Task 1: EnrollmentRecord
# Holds a student object and a timestamp. 
# Worst Case: O(1)
class EnrollmentRecord:
    def __init__(self, student, enroll_date=None):
        self.student = student
        self.enroll_date = enroll_date if enroll_date else date.today().isoformat()

# Task 2: LinkedQueue ADT
# A FIFO Queue implemented using a Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item): # Worst Case: O(1)
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self): # Worst Case: O(1)
        if self.is_empty():
            raise ValueError("Queue is empty: Cannot dequeue.")
        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return data

    def is_empty(self): # Worst Case: O(1)
        return self._size == 0

    def __len__(self): # Worst Case: O(1)
        return self._size

# Task 4 & 5: Algorithms
# Selection Sort: Finds the minimum and swaps it to the front.
def selection_sort(arr, key_func): # Worst Case: O(n^2)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key_func(arr[j]) < key_func(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort: Builds a sorted section one item at a time.
def insertion_sort(arr, key_func): # Worst Case: O(n^2)
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_func(key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

# Recursive Binary Search: Divide and conquer search for sorted data.
def recursive_binary_search(arr, target_id, left, right): # Worst Case: O(log n)
    if left > right:
        return None
    mid = (left + right) // 2
    current_id = arr[mid].student.student_id
    if current_id == target_id:
        return mid
    elif target_id < current_id:
        return recursive_binary_search(arr, target_id, left, mid - 1)
    else:
        return recursive_binary_search(arr, target_id, mid + 1, right)

# Task 3 & 5: Course Logic
class Course:
    def __init__(self, course_code, credits, capacity=30):
        self.course_code = course_code
        self.credits = int(credits)
        self.capacity = int(capacity)
        self.enrolled_roster = []      
        self.waitlist = LinkedQueue()  
        self.enrolled_sorted_by = None 

    # Task 3: Enrollment with Waitlist promotion
    def add_student(self, student_obj, enroll_date=None): # Worst Case: O(n)
        for record in self.enrolled_roster:
            if record.student.student_id == student_obj.student_id:
                return "Already Enrolled"

        new_record = EnrollmentRecord(student_obj, enroll_date)
        if len(self.enrolled_roster) < self.capacity:
            self.enrolled_roster.append(new_record)
            self.enrolled_sorted_by = None 
            return "Enrolled"
        else:
            self.waitlist.enqueue(new_record)
            return "Waitlisted"

    # Task 4: Sorting by ID, Name, or Date
    def sort_enrolled(self, by='id', algorithm='selection'): # Worst Case: O(n^2)
        if by == 'name':
            key_func = lambda x: x.student.name
        elif by == 'date':
            key_func = lambda x: x.enroll_date
        else:
            key_func = lambda x: x.student.student_id
        
        if algorithm == 'insertion':
            insertion_sort(self.enrolled_roster, key_func)
        else:
            selection_sort(self.enrolled_roster, key_func)
        self.enrolled_sorted_by = by

    # Task 5: Drop with Binary Search and Waitlist Promotion
    def drop_student(self, student_id): # Worst Case: O(n^2)
        # Ensure list is sorted by ID for Binary Search
        if self.enrolled_sorted_by != 'id':
            self.sort_enrolled(by='id', algorithm='selection')
        
        idx = recursive_binary_search(self.enrolled_roster, student_id, 0, len(self.enrolled_roster)-1)
        
        if idx is not None:
            self.enrolled_roster.pop(idx)
            # Promote from waitlist if someone is waiting
            if not self.waitlist.is_empty():
                promoted = self.waitlist.dequeue()
                promoted.enroll_date = date.today().isoformat()
                self.enrolled_roster.append(promoted)
                self.enrolled_sorted_by = None 
            return True
        return False

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class University:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def load_from_csv(self, courses_csv, enroll_csv):
        # Load Courses
        with open(courses_csv, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cid = row['course_id']
                self.courses[cid] = Course(cid, row['credits'], row['capacity'])
        
        # Load Enrollments
        with open(enroll_csv, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sid, cid = row['student_id'], row['course_id']
                if sid not in self.students:
                    self.students[sid] = Student(sid, f"Student_{sid}")
                if cid in self.courses:
                    self.courses[cid].add_student(self.students[sid])

if __name__ == "__main__":
    u = University()
    print("University System Initialized (Milestone 2 Tasks 1-5 Complete). - Alex M")