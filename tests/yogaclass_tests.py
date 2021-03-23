import unittest
from models.yogaclass import YogaClass
from models.instructor import Instructor

class TestYogaClass(unittest.TestCase):

    def setUp(self):
        self.instructor1 = Instructor("Schmidt", "07912 123456")
        self.yogaclass = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.", self.instructor1, "2021-03-23", "18:00", 5)
        
    def test_can_count_members(self):
        members = [1, 2, 3, 4, 5]
        self.yogaclass.count_members(members)
        self.assertEqual(5, len(self.yogaclass.members))

    def test_can_check_if_capacity__no_capacity(self):
        members = [1, 2, 3, 4, 5]
        self.yogaclass.check_if_capacity(members)
        self.assertEqual(False, self.yogaclass.available)

    def test_can_check_if_capacity__capacity(self):
        members = [1, 2, 3, 4]
        self.yogaclass.check_if_capacity(members)
        self.assertEqual(True, self.yogaclass.available)    

  