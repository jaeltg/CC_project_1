import unittest
from models.booking import Booking
from models.member import Member
from models.yogaclass import YogaClass
from models.instructor import Instructor
from models.memb_type import MembType

class TestBookings(unittest.TestCase):

    def setUp(self):
        self.instructor1 = Instructor("Schmidt", "07912 123456")
        self.yogaclass = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.", self.instructor1, "2021-03-23", "18:00", 5)
        self.memb_type1 = MembType("Standard")
        self.member1 = Member("https://static0.srcdn.com/wordpress/wp-content/uploads/2020/04/Jess-New-Girl-FEATURED-Cropped.jpg","Jessica Day", "1982-02-13", 6540003, self.memb_type1, "The Loft, LA", "07911 123444")
        self.booking = Booking(self.member1, self.yogaclass)

    def test_can_check_if_capacity__no_capacity(self):
        members = [1, 2, 3, 4, 5]
        self.booking.check_if_capacity(members)
        self.assertEqual(False, self.booking.available)

    def test_can_check_if_capacity__capacity(self):
        members = [1, 2, 3, 4]
        self.booking.check_if_capacity(members)
        self.assertEqual(True, self.booking.available)
