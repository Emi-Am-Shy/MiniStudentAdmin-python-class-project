#ALL WORK BELOW DONE BY SHIYA, CORRECTED BY ALEX
"""
CSE 2050 – Milestone 2 Demo Script
This script walks through the major features required for Milestone 2:
 - Enrolling students until capacity is reached
 - Adding extra students to the waitlist
 - Sorting the enrolled roster
 - Dropping a student using recursive binary search
 - Automatically promoting the next student from the waitlist

Run this file during lab check-off to show the TA the full workflow.
"""

# Import from logic file
from MiniStudentAdmin import Course, Student

print("\n======================================")
print("        Milestone 2 Demo Start")
print("======================================\n")

# Worst Case: O(1)
course = Course("CSE2050", credits=3, capacity=2)

# 2. Create students (ID order 102, 101, 103 to demonstrate sorting)
s1 = Student("102", "Alice")
s2 = Student("101", "Bob")
s3 = Student("103", "Charlie")

print(">>> STEP 1: Enrolling students into CSE2050 (Capacity: 2)...")
print(f"Adding Alice (ID: 102): {course.add_student(s1)}")
print(f"Adding Bob   (ID: 101): {course.add_student(s2)}")
print(f"Adding Charlie (ID: 103): {course.add_student(s3)} (Should be Waitlisted)")

print("\n--- Current Roster ---")
for rec in course.enrolled_roster:
    print(f" Enrolled: {rec.student.student_id} - {rec.student.name}")

print(f"Waitlist Count: {len(course.waitlist)}")

# 3. Sorting demonstration
print("\n>>> STEP 2: Sorting roster by student ID (Selection Sort)...")
# Bob (101) should move to index 0
course.sort_enrolled(by="id", algorithm="selection")

print("Sorted Roster (By ID):")
for rec in course.enrolled_roster:
    print(f" - {rec.student.student_id}: {rec.student.name}")

# 4. Drop demonstration
print("\n>>> STEP 3: Dropping Alice (ID: 102)...")
print("This uses recursive binary search O(log n) and promotes Charlie O(1).")

# This will trigger the binary search inside drop_student
success = course.drop_student("102")

if success:
    print("\nDrop Successful!")
    print("--- Updated Roster (Charlie should now be included) ---")
    for rec in course.enrolled_roster:
        print(f" - {rec.student.student_id}: {rec.student.name}")
    
    print(f"Waitlist Count now: {len(course.waitlist)}")
else:
    print("Drop failed: Student not found.")

print("\n======================================")
print("        Milestone 2 Demo Complete")
print("======================================\n")
