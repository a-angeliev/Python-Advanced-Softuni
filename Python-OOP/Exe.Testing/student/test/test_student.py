from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test")
        self.student1 = Student("Test1", {"python": []})

    def test_obj_created(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_adding_existing_course(self):
        result = self.student1.enroll("python", ["python is a good language", "Hi python"], '')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["python is a good language", "Hi python"], self.student1.courses["python"])

    def test_adding_new_course_with_notes(self):
        result = self.student.enroll("python", ["python is a good language", "Hi python"], '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["python is a good language", "Hi python"], self.student.courses["python"])

    def test_adding_new_course_with_note(self):
        result = self.student.enroll("python", ["python is a good language", "Hi python"], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["python is a good language", "Hi python"], self.student.courses["python"])

    def test_adding_new_course_without_notes(self):
        result = self.student.enroll("python", ["python is a good language", "Hi python"], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["python"])

    def test_adding_notes_in_existing_course(self):
        result = self.student1.add_notes("python", "Hi python")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['Hi python'], self.student1.courses["python"])

    def test_adding_notest_in_unexisting_course_exception_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("C++", "some notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaveing_existing_course(self):
        result = self.student1.leave_course("python")
        self.assertEqual({}, self.student1.courses)
        self.assertEqual("Course has been removed", result)

    def test_leaveing_unexisting_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()
