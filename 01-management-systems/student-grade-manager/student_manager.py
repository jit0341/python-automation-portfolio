# school/students.py

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # exam_marks = { exam_type: { subject: marks } }
        self.exam_marks = {}

    def add_mark(self, exam_type, subject, marks):
        """Add marks for a subject in a particular exam."""
        if exam_type not in self.exam_marks:
            self.exam_marks[exam_type] = {}
        self.exam_marks[exam_type][subject] = marks

    def get_marks(self, exam_type):
        """Return marks of a particular exam."""
        return self.exam_marks.get(exam_type, {})

    def __str__(self):
        return f"Student: {self.name}, Grade: {self.grade}"
