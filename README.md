# MiniStudentAdmin-python-class-project
This is a class projects which makes use of Object Oriented Programming to efficiently and professionally make a miniature student administration system to manage course credits, courses, and individual students on a large scale. Ensureing efficient processing of computation via; time, use of resources, and Anatomic Opperations(Big-O).

CSE2025: Milestone #1

Lab Participants: Juan Alexander Morquecho Velazquez & Shiya Subbaiah

Project Overview

This project makes use of Object-Oriented Programming (OOP) to efficiently asses and create a miniature student administration system. It is designed to manage course credits, rosters, and individual student grades on a large scale.

Core Python Modules import csv: A built-in module designed to efficiently read and translate CSV files. Using DictReader, we transform raw text into Python dictionaries, allowing us to access data by column headers (like 'student_id') rather than index numbers.import statistics: Provides predefined mathematical methods. Instead of manually calculating averages, we use statistics.mean() and statistics.median() to ensure high reliability with floating-point numbers—crucial for accurate grading systems.

System Architecture1. The Course ClassRepresents a single course in the university catalog (e.g., "CSE2050").Attributes: course_code (String), credits (Int), and students (List of Student Objects).Security Measure: In add_student(), we use if student_obj not in self.students. This checks the Object Identity (memory address) to prevent duplicate enrollments.2. The Student ClassRepresents an individual student and their academic history.Data Gatekeeper: The __init__ method ensures all IDs are exactly 8 characters and start with "STU". It also prevents empty names using .strip().Object Association: In the enroll() method, the Student "talks" to the Course object by calling course_obj.add_student(self). This links the two objects together in memory.GPA Engine: Uses a $O(n)$ loop to calculate a weighted GPA:$$GPA = \frac{\sum(\text{grade points} \times \text{credits})}{\sum\text{credits}}$$It includes a "Safety Shield" (if total_cr > 0) to prevent program crashes caused by division by zero.3. The University ClassThe central manager that stores all objects in dictionaries for fast lookup.Fast Lookups: Uses self.students = {} and self.courses = {}. Checking if a key exists in a dictionary is $O(1)$, meaning it stays lightning-fast regardless of how many students are added.Analytical Methods: Includes logic for finding the intersection of students between two courses and calculating university-wide statistics.

Computational Efficiency |
How to RunPrepare Data: Ensure course_catalog(in).csv and university_data(in).csv are in the project folder.Execution: Run python MiniStudentAdmin.py to load the data.Testing: Run python Test_MiniStudentAdmin.py to execute the unit tests and verify the logic.

Lab Partner Note "Hai Shiya! I'm like super sleepy yet so energized right now but I wanted to say I love you platonically and I appreciate you as my lab partner :3 You're a goated lab partner! :DD"