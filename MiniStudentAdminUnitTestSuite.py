"""
CSE 2050 – Milestone 2
Unit Test Suite (Task 6)

This file contains tests for:
 - LinkedQueue (FIFO behavior, size tracking, error handling)
 - Enrollment + waitlist logic
 - Sorting by ID, name, and date
 - Recursive binary search
"""

import unittest
from datetime import date

# Import everything from your logic file
from MiniStudentAdmin import (
    LinkedQueue, Course, Student, EnrollmentRecord, 
    recursive_binary_search
)
#ALL WORK BELOW DONE BY SHIYA, CORRECTED BY ALEX

# ============================================================
#   TEST 1: LinkedQueue (Task 2)
# ============================================================
class TestLinkedQueue(unittest.TestCase):
    """Tests for the LinkedQueue ADT (FIFO queue using linked list)."""

    def test_enqueue_dequeue_fifo(self):
        """Ensure items come out in the same order they went in (FIFO)."""
        q = LinkedQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

    def test_dequeue_empty_raises(self):
        """Dequeue on an empty queue should raise ValueError."""
        q = LinkedQueue()
        with self.assertRaises(ValueError):
            q.dequeue()

    def test_queue_length(self):
        """Verify that __len__ correctly tracks queue size."""
        q = LinkedQueue()
        q.enqueue("A")
        q.enqueue("B")
        self.assertEqual(len(q), 2)

        q.dequeue()
        self.assertEqual(len(q), 1)


# ============================================================
#   TEST 2: Enrollment + Waitlist (Task 3)
# ============================================================
class TestEnrollment(unittest.TestCase):
    """Tests for course capacity, enrollment, and waitlist promotion."""

    def test_capacity_and_waitlist(self):
        """
        Enroll up to capacity → extra students should go to waitlist.
        """
        course = Course("CSE2050", 3, capacity=2)

        s1 = Student("1", "Alice")
        s2 = Student("2", "Bob")
        s3 = Student("3", "Charlie")

        self.assertEqual(course.add_student(s1), "Enrolled")
        self.assertEqual(course.add_student(s2), "Enrolled")
        self.assertEqual(course.add_student(s3), "Waitlisted")

        self.assertEqual(len(course.enrolled_roster), 2)
        self.assertEqual(len(course.waitlist), 1)

    def test_drop_promotes_waitlisted(self):
        """
        Dropping an enrolled student should automatically enroll
        the next student from the waitlist (FIFO).
        """
        course = Course("CSE2050", 3, capacity=1)

        s1 = Student("1", "Alice")
        s2 = Student("2", "Bob")

        course.add_student(s1)
        course.add_student(s2)  # goes to waitlist

        # Drop student "1". This internally sorts and promotes from waitlist.
        course.drop_student("1")

        self.assertEqual(len(course.enrolled_roster), 1)
        self.assertEqual(course.enrolled_roster[0].student.student_id, "2")


# ============================================================
#   TEST 3: Sorting (Task 4)
# ============================================================
class TestSorting(unittest.TestCase):
    """Tests for sorting by ID, name, and date using both algorithms."""

    def test_sort_by_id_selection(self):
        """Selection sort should correctly order students by ID."""
        s1 = Student("3", "Charlie")
        s2 = Student("1", "Alice")
        s3 = Student("2", "Bob")

        course = Course("CSE2050", 3, capacity=10)
        course.add_student(s1)
        course.add_student(s2)
        course.add_student(s3)

        course.sort_enrolled(by="id", algorithm="selection")

        ids = [rec.student.student_id for rec in course.enrolled_roster]
        self.assertEqual(ids, ["1", "2", "3"])

    def test_sort_by_name_insertion(self):
        """Insertion sort should correctly order students alphabetically."""
        s1 = Student("3", "Charlie")
        s2 = Student("1", "Alice")
        s3 = Student("2", "Bob")

        course = Course("CSE2050", 3, capacity=10)
        course.add_student(s1)
        course.add_student(s2)
        course.add_student(s3)

        course.sort_enrolled(by="name", algorithm="insertion")

        names = [rec.student.name for rec in course.enrolled_roster]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])


# ============================================================
#   TEST 4: Recursive Binary Search (Task 5)
# ============================================================
class TestBinarySearch(unittest.TestCase):
    """Tests for recursive binary search over EnrollmentRecord lists."""

    def test_binary_search_found(self):
        """Binary search should return correct index when ID exists."""
        s1 = Student("1", "Alice")
        s2 = Student("2", "Bob")
        s3 = Student("3", "Charlie")

        arr = [
            EnrollmentRecord(s1),
            EnrollmentRecord(s2),
            EnrollmentRecord(s3)
        ]

        # Array must be sorted by the key we are searching (ID)
        idx = recursive_binary_search(arr, "2", 0, 2)
        self.assertEqual(idx, 1)

    def test_binary_search_not_found(self):
        """Binary search should return None when ID is not present."""
        s1 = Student("1", "Alice")
        s2 = Student("2", "Bob")

        arr = [
            EnrollmentRecord(s1),
            EnrollmentRecord(s2)
        ]

        idx = recursive_binary_search(arr, "999", 0, 1)
        self.assertIsNone(idx)


# ============================================================
#   MAIN
# ============================================================
if __name__ == "__main__":
    unittest.main()