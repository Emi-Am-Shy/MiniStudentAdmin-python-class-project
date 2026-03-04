import unittest
from MiniStudentAdmin import Student, Course, University

class Test_MiniStudentAdmin(unittest.TestCase):

    def setUp(self):
        self.uni = University()
        self.c1 = Course("CSE1010", 3)
        self.s1 = Student("STU00001", "Alice")

    # Course Tests
    def test_course_roster(self):
        self.c1.add_student(self.s1)
        self.assertEqual(self.c1.get_student_count(), 1)
        # Prevent duplicates
        self.c1.add_student(self.s1)
        self.assertEqual(self.c1.get_student_count(), 1)

    # Student Tests
    def test_gpa(self):
        c2 = Course("MATH1010", 3)
        self.s1.enroll(self.c1, "A")  # 4.0 * 3
        self.s1.enroll(c2, "B")       # 3.0 * 3
        # (12 + 9) / 6 = 3.5
        self.assertEqual(self.s1.calculate_gpa(), 3.5)

    def test_invalid_id(self):
        with self.assertRaises(ValueError):
            Student("NOT_STU", "Bob")

    # University Tests
    def test_duplicate_entities(self):
        self.uni.add_student("STU12345", "Dave")
        self.uni.add_student("STU12345", "Dave")
        self.assertEqual(len(self.uni.students), 1)

    def test_lookups(self):
        self.assertIsNone(self.uni.get_student("STU99999"))
        self.assertIsNone(self.uni.get_course("FAKE101"))

if __name__ == "__main__":
    unittest.main()