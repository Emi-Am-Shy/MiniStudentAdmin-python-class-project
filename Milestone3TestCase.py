import unittest
from milestone3 import HashMap, Course, Student, University

class TestMilestone3(unittest.TestCase):

    def setUp(self): #Alex
        """Set up a fresh environment for each test."""
        self.h_map = HashMap(initial_size=5)
        self.student = Student("101", "Alex Morquecho")
        self.course = Course("CSE2102", 3, capacity=2)
        # Manually adding a prerequisite for testing
        self.course.add_prerequisite("CSE2102", "CSE1010")

    # --- HashMap Tests --- #Alex
    def test_hashmap_put_get(self):
        """Test basic insertion and retrieval."""
        self.h_map.put("CSE1010", "Introduction to Computing")
        self.assertEqual(self.h_map.get("CSE1010"), "Introduction to Computing")

    def test_hashmap_collision_and_rehash(self):#Alex
        """Test that data survives rehashing at 80% load."""
        # Initial size is 5, 80% is 4. Adding 5 items will trigger rehash.
        items = [("C1", "V1"), ("C2", "V2"), ("C3", "V3"), ("C4", "V4"), ("C5", "V5")]
        for k, v in items:
            self.h_map.put(k, v)
        
        # Verify all items still exist after the table doubled in size
        for k, v in items:
            self.assertEqual(self.h_map.get(k), v)
        self.assertEqual(self.h_map.size, 10)

    # --- Enrollment & Prerequisite Tests ---
    def test_prerequisite_failure(self): #Shiya
        """Test that an Exception is raised if the student lacks the prerequisite."""
        # Student hasn't taken CSE1010, should fail
        with self.assertRaises(Exception) as context:
            self.course.request_enroll(self.student)
        self.assertTrue("Prerequisite Error" in str(context.exception))

    def test_prerequisite_success(self): #Shiya
        """Test that enrollment works once the prerequisite is met."""
        self.student.completed_courses.append("CSE1010")
        result = self.course.request_enroll(self.student)
        self.assertEqual(result, "Enrolled")
        self.assertEqual(len(self.course.enrolled_roster), 1)

    # --- Sorting Tests ---
    def test_merge_sort_by_id(self): #Shiya
        """Test that the roster correctly sorts by Student ID."""
        s1 = Student("999", "Zelda")
        s2 = Student("111", "Alice")
        s3 = Student("555", "Bob")
        
        # Manually bypass enrollment checks to fill roster
        from milestone3 import EnrollmentRecord
        self.course.enrolled_roster = [
            EnrollmentRecord(s1),
            EnrollmentRecord(s2),
            EnrollmentRecord(s3)
        ]
        
        self.course.sort_roster(by='id')
        
        # Check order: 111, 555, 999
        ids = [record.student.student_id for record in self.course.enrolled_roster]
        self.assertEqual(ids, ["111", "555", "999"])

if __name__ == '__main__':
    unittest.main()