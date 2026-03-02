import unittest
import MiniStudentAdmin

class Test_MiniStudentAdmin(unittest.TestCase):
    def test_Student_init_(self):
        pass
    
    def test_Course_init_(self):
        course1 = MiniStudentAdmin.Course("CSE2050", 4, [])
        self.assertIsInstance(course1.course_code, str)
        self.assertEqual(course1.course_code, "CSE2025")

        self.assertIsInstance(course1.credits, int)
        self.assertEqual(course1.credits, 4)
        
        self.assertIsInstance(course1.students, list)
        self.assertEqual(course1.students, [])

        student1 = MiniStudentAdmin.Student("abc12002", "Name", dict{CSE2050})
        course1 = MiniStudentAdmin.Course("CSE2050", 4, [])
        pass

    def test_add_students(self):
        course1 = MiniStudentAdmin.Course("CSE2050", 4, [])
        
        pass

    def test_get_student_count(self):
        pass




if __name__ == "__main__":  
    unittest.main()