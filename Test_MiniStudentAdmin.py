import unittest
from MiniStudentAdmin import Student, Course, University

class Test_MiniStudentAdmin(unittest.TestCase):

    def setUp(self):
        """Initializes a fresh university, course, and student instance before each individual test runs."""
        self.uni = University()
        self.c1 = Course("CSE1010", 3)
        self.s1 = Student("STU00001", "Alice")

    # Course Tests
    def test_course_roster(self):
        """Verifies that students are correctly added to the roster and that duplicate entries are blocked."""
        self.c1.add_student(self.s1)
        self.assertEqual(self.c1.get_student_count(), 1)
        # Prevent duplicates
        self.c1.add_student(self.s1)
        self.assertEqual(self.c1.get_student_count(), 1)

    # Student Tests
    def test_gpa(self):
        """Confirms the weighted GPA calculation correctly processes multiple courses and credit values."""
        c2 = Course("MATH1010", 3)
        self.s1.enroll(self.c1, "A")  # 4.0 * 3
        self.s1.enroll(c2, "B")       # 3.0 * 3
        # (12 + 9) / 6 = 3.5
        self.assertEqual(self.s1.calculate_gpa(), 3.5)

    def test_invalid_id(self):
        """Ensures the program raises a ValueError when a student ID fails the format security check."""
        with self.assertRaises(ValueError):
            Student("NOT_STU", "Bob")

    # University Tests
    def test_duplicate_entities(self):
        """Checks that the University dictionary prevents creating multiple student records for the same ID."""
        self.uni.add_student("STU12345", "Dave")
        self.uni.add_student("STU12345", "Dave")
        self.assertEqual(len(self.uni.students), 1)

    def test_lookups(self):
        """Validates that search methods return None when a student or course does not exist in the system."""
        self.assertIsNone(self.uni.get_student("STU99999"))
        self.assertIsNone(self.uni.get_course("FAKE101"))

if __name__ == "__main__":
    unittest.main()