# MiniStudentAdmin-python-class-project
University Management System - Milestone 3

This project makes use of Object-Oriented Programming (OOP) to create a professional student administration system. It is designed to manage course credits, rosters, and individual student grades on a large scale, ensuring efficient processing via Algorithmic Analysis (Big-O).

## Lab Participants
* **Juan Alexander Morquecho Velazquez**
* **Shiya Subbaiah**

# University Enrollment System - Milestone 3 
**Date:** April 22, 2026  

## --------------------------------------------------------------------------------

## Project Overview
Milestone 3 focuses on optimizing the University Enrollment System by replacing basic list-based searches and inefficient sorting algorithms with professional-grade data structures. The system now utilizes a custom **HashMap** for prerequisite verification and **Merge Sort** for roster management, ensuring the system can scale to handle thousands of students and courses with minimal performance lag due to time efficient abstract data structures. 

## Key Components & Data Structures

### 1. Custom HashMap (Separate Chaining)
To keep lookups fast, I implemented a HashMap. 
* **Collision Handling:** Uses **Separate Chaining** (linked buckets) to handle hash collisions.
* **Dynamic Resizing:** Automatically triggers a `_rehash()` operation when the **Load Factor reaches 80%**, doubling the table size to maintain O(1) performance.
* **Primary Use:** Fast verification of course prerequisites during enrollment.

### 2. Merge Sort
Replaced Milestone 2’s Selection/Insertion sorts with a **Divide and Conquer** algorithm.
* **Stability:** Unlike Quick Sort, Merge Sort is stable, preserving the relative order of students who might have identical sorting keys (e.g., same enrollment date).
* **Guaranteed Performance:** Provides a consistent O(nlogn) time complexity even on worst-case data.

### 3. LinkedQueue (Waitlist Management)
The course waitlist uses a custom Linked List implementation.
* **Efficiency:** Features both a `_head` and `_tail` pointer, allowing for O(1) additions (`enqueue`) and O(1) removals (`dequeue`).

## How to Use

### Data Loading
The system is designed to ingest data from CSV files. **Important:** Prerequisites must be loaded before enrollment data to ensure the verification logic functions correctly.

  uni = University()
# Load prerequisites first so they are available for validation
  uni.load_prerequisites('prerequisites.csv')
# Load courses and student enrollments
uni.load_university_data('courses.csv', 'enrollments.csv')

# -----------------------------------------------------------------------------------------------------------------------------

## TestCase Overview
This test suite utilizes the Python `unittest` framework to verify that the optimized data structures implemented in Milestone 3 function correctly under various conditions, including edge cases like hash collisions and enrollment rejections.

## Test Categories

### 1. HashMap & Data Integrity
* **`test_hashmap_put_get`**: Verifies basic key-value storage. Confirms that data written to the `HashMap` can be retrieved accurately.
* **`test_hashmap_collision_and_rehash`**: 
    * Validates the **80% Load Factor** trigger. 
    * Ensures that when the table size doubles (from 5 to 10), all existing data is correctly re-indexed and remains accessible.

### 2. Enrollment Logic (Prerequisite Engine)
* **`test_prerequisite_failure`**: Confirms that the system correctly raises an `Exception` when a student attempts to enroll in a course without meeting the requirements stored in the `HashMap`.
* **`test_prerequisite_success`**: Verifies that once the required course ID is added to the student's `completed_courses` list, the `request_enroll` method transitions from "Error" to "Enrolled."

### 3. Algorithm Validation (Merge Sort)
* **`test_merge_sort_by_id`**: 
    * Tests the `merge_sort` implementation by providing an unsorted list of Student IDs (`999`, `111`, `555`).
    * Confirms the final roster is ordered correctly (`111` -> `555` -> `999`).
    * Validates that the `key_func` correctly accesses nested `Student` object attributes within `EnrollmentRecord` objects.

## How to Run  Tests

To run the tests and view the results for your lab check, you can use this command in the terminnal:

```bash
python test_milestone3.py