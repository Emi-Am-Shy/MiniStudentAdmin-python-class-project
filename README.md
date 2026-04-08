# MiniStudentAdmin-python-class-project
University Management System - Milestone 1

This project makes use of Object-Oriented Programming (OOP) to create a professional student administration system. It is designed to manage course credits, rosters, and individual student grades on a large scale, ensuring efficient processing via Algorithmic Analysis (Big-O).

## Lab Participants
* **Juan Alexander Morquecho Velazquez**
* **Shiya Subbaiah**

## Core Python Modules
* **import csv:** A built-in module designed to efficiently read and translate CSV files. Using `DictReader`, we transform raw text into Python dictionaries, allowing us to access data by column headers (like 'student_id') rather than index numbers.
* **import statistics:** Provides predefined mathematical methods. Instead of manually calculating averages, we use `statistics.mean()` and `statistics.median()` to ensure high reliability—crucial for accurate grading systems.

## System Architecture

### 1. The Course Class
Represents a single course in the university catalog (e.g., "CSE2050").
* **Attributes:** `course_code` (String), `credits` (Int), and `students` (List of Student Objects).
* **Security Measure:** In `add_student()`, we use `if student_obj not in self.students`. This checks the **Object Identity** (memory address) to prevent duplicate enrollments.



### 2. The Student Class
Represents an individual student and their academic history.
* **Data Gatekeeper:** The `__init__` method ensures all IDs are exactly 8 characters and start with "STU". It also prevents empty names using `.strip()`.
* **Object Association:** In the `enroll()` method, the Student "talks" to the Course object by calling `course_obj.add_student(self)`. This links the two objects together in memory.
* **GPA Engine:** Uses an O(n) loop to calculate a weighted GPA.

* **Safety Shield:** Includes a check (`if total_cr > 0`) to prevent program crashes caused by division by zero.

### 3. The University Class
The central manager that stores all objects in dictionaries for fast lookup.
* **Fast Lookups:** Uses `self.students = {}` and `self.courses = {}`. Checking if a key exists in a dictionary is $O(1)$, meaning it stays lightning-fast regardless of how many students are added.
* **Analytical Methods:** Includes logic for finding the intersection of students between two courses and calculating university-wide statistics.

### Computational Efficiency
**How to RunPrepare Data**: Ensure course_catalog(in).csv and university_data(in).csv are in the project folder.Execution: Run python MiniStudentAdmin.py to load the data.Testing: Run python Test_MiniStudentAdmin.py to execute the unit tests and verify the logic.

 "Hai Shiya! I'm like super sleepy yet so energized right now but I wanted to say I love you platonically and I appreciate you as my lab partner :3 You're a goated lab partner! :DD"

## Milestone 2 Task Implementation Explanations:

### 1. The LinkedQueue (The Waitlist)
This implements a FIFO (First-In, First-Out) queue using a Linked List. 

 - This is more efficient than a Python list for queues because dequeue is O(1) instead of O(n).

 - **class Node:** The building block. 

    . Each node holds data (a student record) and a next pointer to the person behind them.
    
    . **enqueue(item):** Creates a Node. (If the queue is empty, both head and tail point to it.)
    
    . Otherwise, it sticks the new node after the current _tail and moves the tail pointer to the new end.
    
    . **dequeue():** Saves the data from _head. Moves _head one step forward (self._head = self._head.next). If the last person was removed, it sets _tail to None.

---

## Key Features & Algorithms

### Sorting the Roster
The system supports sorting the `enrolled_roster` of `EnrollmentRecord` objects by **Student Name**, **Student ID**, or **Enrollment Date**. 

* **Algorithms Implemented:** Selection Sort and Insertion Sort (O(n^2)).
* **State Tracking:** The `Course` object tracks which attribute it is currently sorted by to determine if efficient searching is possible.

### Recursive Binary Search
When a student needs to be dropped from a course that is already sorted by Student ID, the system employs a **Recursive Binary Search** (O(log n)). This allows for high-performance lookups in large datasets compared to a standard linear search.

### Automatic Enrollment Logic
* **Capacity Check:** If a course is full, students are automatically added to the `LinkedQueue` (FIFO).
* **Auto-Fill:** When a student is successfully dropped, the `Course` automatically `dequeue`s the next student from the waitlist and moves them into the `enrolled_roster`.

## Data Structures Summary

| Task | Data Structure | Complexity |
| :--- | :--- | :--- |
| **Waitlist** | Linked List (Queue ADT) | O(1) Enqueue/Dequeue |
| **Search (by ID)** | Recursive Binary Search | O(\log n) |
| **Sorting** | Selection & Insertion Sort | O(n^2) |
| **Student Record** | EnrollmentRecord Wrapper | N/A |

## Usage
To initialize the system and load data, ensure your CSV files are in the root directory and use the `University` class:

======================
Shiya's Read me Below
======================

Milestone 2 – Complexity Reflection
CSE 2050 – Spring 2026

This milestone added several new data‑structure concepts on top of our Milestone 1 system.
Below is a short summary of the time complexities for the structures and algorithms we implemented,
along with a quick explanation of why they behave the way they do.

1. LinkedQueue (enqueue and dequeue)
Our LinkedQueue uses a simple singly linked list with both a head and a tail pointer. Because of that:
• enqueue(item): O(1)
  We always insert at the tail, and since we keep a direct pointer to it, no traversal is needed.
• dequeue(): O(1)
  We remove from the head, which is also just a pointer update.

This is one of the main benefits of using a linked list for a queue — both operations stay constant time.

2. Sorting Algorithms
We implemented Selection Sort and Insertion Sort.

• Selection Sort: O(n^2)
  It always scans the remaining unsorted portion of the list to find the minimum. Even if the list is
  already sorted, it still does the same number of comparisons.

• Insertion Sort: O(n^2) worst case, but O(n) best case
  The worst case happens when the list is in reverse order and every element has to shift all the way
  to the front. But if the list is already sorted (or close to it), Insertion Sort is much faster because
  each element only moves a little.

3. Recursive Binary Search
• Time Complexity: O(log n)
  Each recursive call cuts the search space in half, which is why binary search is so efficient.

• Why sorting is required:
  Binary search only works if the list is sorted. Without sorting, the comparison at the midpoint
  doesn’t tell us which half of the list to discard, so the algorithm would not work correctly.

4. Comparing the Sorting Algorithms
Selection Sort is predictable but slow — it always does the same amount of work. Insertion Sort, on the
other hand, can be much faster when the data is already partially sorted. In practice, Insertion Sort is
usually the better choice for small or nearly sorted lists, while Selection Sort is mainly useful for its
simplicity and consistency.