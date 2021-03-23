import unittest
from models.yogaclass import YogaClass
from models.instructor import Instructor

class TestYogaClass(unittest.TestCase):

    def test_can_count_members(self):
        members = [1, 2, 3, 4, 5]
        instructor1 = Instructor("Schmidt", "07912 123456")
        yogaclass = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.", instructor1, "2021-03-23", "18:00", 10)
        yogaclass.count_members(members)
        self.assertEqual(5, len(yogaclass.members))

