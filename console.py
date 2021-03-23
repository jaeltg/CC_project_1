import pdb
from models.yogaclass import YogaClass
from models.member import Member
from models.booking import Booking
from models.instructor import Instructor

import repositories.yogaclass_repository as yogaclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.instructor_repository as instructor_repository

booking_repository.delete_all()
yogaclass_repository.delete_all()
member_repository.delete_all()
instructor_repository.delete_all()

member1 = Member("Jessica Day", "1982-02-13", 6540003, "Standard", "The Loft, LA", "07911 123444")
member_repository.save(member1)

member2 = Member("Nick Miller", "1990-09-29", 7800643, "Standard", "The Loft, LA", "07912 123456")
member_repository.save(member2)

instructor1 = Instructor("Schmidt", "07912 123456")
instructor_repository.save(instructor1)

yogaclass1 = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.", instructor1, "2021-03-23", "18:00", 10)
yogaclass_repository.save(yogaclass1)

yogaclass2 = YogaClass("Power Yoga", 45, "Fast paced class focussing  more on core and upper body work to increase stamina, flexibility and strength.", instructor1, "2021-03-23", "13:00", 10)
yogaclass_repository.save(yogaclass2)

booking1 = Booking(member1, yogaclass1)
booking_repository.save(booking1)

booking2 = Booking(member1, yogaclass2)
booking_repository.save(booking2)

pdb.set_trace()