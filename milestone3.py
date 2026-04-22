#--------------------------------------------------------------------
# Milestone 3 System - Updated for Lab 4/22
#--------------------------------------------------------------------

from datetime import date
import csv

# Task 1: HashMap with Separate Chaining and Rehashing
class HashMap:
    """
    Its purpose is to store prerequisites from each course
    This table functions simlar to a dictionary, 
    but more efficent and uses sperate chainging to handle hash collisions
    
    """
    def __init__(self, initial_size=5):
        self.size = initial_size
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key): #Avg: O(1), Best:O(1), Worst:O(n) (n is length of the key)
        """check load factor"""
        return hash(key) % self.size

    def put(self, key, value): # Avg:O(1), Best:O(1), Worst(n)
        """allows user to input value"""
        # Check load factor (80%)
        if self.count / self.size >= 0.8:
            self._rehash()

        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.buckets[index].append([key, value])
        self.count += 1

    def get(self, key): #Avg:O(1), Best:O(1), Worst:O(n)
        """alows for user to access data"""
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def _rehash(self): #Avg:O(n), Best:O(n), Worst:O(n)
        """rehash hash map when load factor at or above 80%"""
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

def merge_sort(arr, key_func): #Avg:O(nlogn), Best:O(nlogn), Worst:O(nlogn)
    """Replacement for Selection/Insertion Sort, efficient and a good standard sorting alg overall"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key_func)
        merge_sort(right_half, key_func)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if key_func(left_half[i]) <= key_func(right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

class EnrollmentRecord:
    def __init__(self, student, enroll_date=None):
        self.student = student
        self.enroll_date = enroll_date if enroll_date else date.today().isoformat()

class Node:
    def __init__(self, data):
        """wrapper pattern for node"""
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item): #Avg:O(1), Best:O(1), Worst:O(1)
        """efficeint enque implementaion in bucket chain"""
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self): #Avg:O(1), Best:O(1), Worst:O(1)
        """efficeint deque implementaion in bucket chain"""
        if self.is_empty():
            raise ValueError("Queue is empty.")
        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return data

    def is_empty(self): #Avg:O(1), Best:O(1), Worst:O(1)
        """Returns size"""
        return self._size == 0

    def __len__(self): #Avg:O(1), Best:O(1), Worst:O(1)
        """returns length"""
        return self._size

class Student:
    """Tracks courses completed (Prerequisite check)"""
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.completed_courses = [] 

class Course:
    def __init__(self, course_code, credits, capacity=30):
        self.course_code = course_code
        self.credits = int(credits)
        self.capacity = int(capacity)
        self.enrolled_roster = []
        self.waitlist = LinkedQueue()
        # Task 2: Prerequisite HashMap
        self.prerequisites = HashMap()

    def add_prerequisite(self, course_id, prereq_id): #Avg:O(1), Best:O(1), Worst:O(n)
        self.prerequisites.put(course_id, prereq_id)

    def request_enroll(self, student_obj): #Avg:O(n) number of students enrolled in specific course, Best:O(1), Worst:O(n)
        """Prerequisite Verification"""
        required_prereq = self.prerequisites.get(self.course_code)
        
        if required_prereq and required_prereq not in student_obj.completed_courses:
            raise Exception(f"Prerequisite Error: {student_obj.name} has not completed {required_prereq}")

        # Check for duplicates
        for record in self.enrolled_roster:
            if record.student.student_id == student_obj.student_id:
                return "Already Enrolled"

        new_record = EnrollmentRecord(student_obj)
        if len(self.enrolled_roster) < self.capacity:
            self.enrolled_roster.append(new_record)
            return "Enrolled"
        else:
            self.waitlist.enqueue(new_record)
            return "Waitlisted"

    def sort_roster(self, by='id'): #Avg:O(nlogn), Best:O(nlogn), Worst:O(nlogn)
        """Sorts the roster using different methods"""
        if by == 'name':
            key_func = lambda x: x.student.name
        elif by == 'date':
            key_func = lambda x: x.enroll_date
        else:
            key_func = lambda x: x.student.student_id
        
        merge_sort(self.enrolled_roster, key_func)

class University:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def load_prerequisites(self, prereq_csv): #Avg:O(n), Best:O(n), Worst:O(n)
        """Loads prerequisits"""
        with open(prereq_csv, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cid = row['course_id']
                pid = row['prerequisite_id']
                if cid in self.courses:
                    self.courses[cid].add_prerequisite(cid, pid)

    def load_university_data(self, courses_csv, enroll_csv): #Avg:O(n + m), Best:O(n + m * k), Worst:O(n^2 + m * k)
                                                             #K is because of request enroll which contains a loop to check for dublicates
        """Implementation for loading Course and Student objects from CSV"""
        # 1. Load Courses
        with open(courses_csv, mode='r', encoding='utf-8-sig') as f: #O(n) = number of rows
            reader = csv.DictReader(f)
            for row in reader:
                cid = row['course_id']
                # Use the capacity from the CSV if it exists, otherwise default to 30
                cap = row.get('capacity', 30)
                creds = row.get('credits', 3)
                self.courses[cid] = Course(cid, creds, cap)
        
        # 2. Load Students and initial Enrollments
        with open(enroll_csv, mode='r', encoding='utf-8-sig') as f: #O(m) = number of rows 
            reader = csv.DictReader(f)
            for row in reader:
                sid = row['student_id']
                cid = row['course_id']
                
                # If we haven't seen this student yet, create them
                if sid not in self.students:
                    # For now, we use a placeholder name like 'Student_ID'
                    self.students[sid] = Student(sid, f"Student_{sid}")
                
                # Enroll the student into the course
                if cid in self.courses:
                    try:
                        # In a real scenario, you'd load completed courses first
                        # to ensure they pass the prerequisite check
                        self.courses[cid].request_enroll(self.students[sid])
                    except Exception as e:
                        print(f"Initial load error for Student {sid} in {cid}: {e}")

if __name__ == "__main__":
    print("Milestone 3 Logic Ready for Lab Check - Alex M")