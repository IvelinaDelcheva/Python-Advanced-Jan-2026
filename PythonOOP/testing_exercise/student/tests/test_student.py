from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        self.student1 = Student('Name1', {"Python": ["n1", "n2", "n3"],
                                          "Java": ["n1", "n2"]})
        self.student2 = Student("Name2")

    def test_init(self):
        self.assertEqual('Name1', self.student1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"],
                          "Java": ["n1", "n2"]}, self.student1.courses)

        self.assertEqual('Name2', self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_enroll_course_name_in_courses(self):
        result = self.student1.enroll("Java", ["n3", "n4"])
        self.assertIn("n3", self.student1.courses["Java"])
        self.assertIn("n4", self.student1.courses["Java"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_course_name_not_in_courses(self):
        result = self.student2.enroll("JS", ["n1", "n2"], "Y")
        self.assertEqual({"JS": ["n1", "n2"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)

        result = self.student2.enroll("C#", ["n1", "n2"], "")
        self.assertIn("C#", self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_name_not_in_courses_notes_n(self):
        result = self.student2.enroll("Python", ["n1", "n2"], "N")
        self.assertEqual({"Python": []}, self.student2.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_course_in_courses(self):
        result = self.student1.add_notes("Python", "n5")
        self.assertIn("n5", self.student1.courses['Python'])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_course_not_in_courses(self):
        with self.assertRaises(Exception) as e:
            self.student1.add_notes("JS", "n5")
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))


    def test_leave_course_in_courses(self):
        result = self.student1.leave_course("Python")
        self.assertNotIn("Python", self.student1.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_not_in_courses(self):
        with self.assertRaises(Exception) as e:
            self.student1.leave_course("JS")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))

if __name__ == '__main__':
    main()
