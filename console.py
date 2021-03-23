import pdb
from models.yogaclass import YogaClass
from models.member import Member
from models.booking import Booking
from models.instructor import Instructor
from models.memb_type import MembType

import repositories.yogaclass_repository as yogaclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.instructor_repository as instructor_repository
import repositories.memb_type_repository as memb_type_repository

booking_repository.delete_all()
yogaclass_repository.delete_all()
member_repository.delete_all()
instructor_repository.delete_all()

memb_type1 = MembType("Standard")
memb_type_repository.save(memb_type1)

memb_type2 = MembType("Premium")
memb_type_repository.save(memb_type2)

member1 = Member("https://static0.srcdn.com/wordpress/wp-content/uploads/2020/04/Jess-New-Girl-FEATURED-Cropped.jpg","Jessica Day", "1982-02-13", 6540003, memb_type1, "The Loft, LA", "07911 123444")
member_repository.save(member1)

member2 = Member("https://static0.srcdn.com/wordpress/wp-content/uploads/2020/04/Jess-New-Girl-FEATURED-Cropped.jpg","Nick Miller", "1990-09-29", 7800643, memb_type1, "The Loft, LA", "07912 123456")
member_repository.save(member2)

instructor1 = Instructor("Schmidt", "07912 123456")
instructor_repository.save(instructor1)

yogaclass1 = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.", instructor1, "2021-03-23", "18:00", 10)
yogaclass_repository.save(yogaclass1)

yogaclass2 = YogaClass("Power Yoga", 45, "Fast paced class focussing  more on core and upper body work to increase stamina, flexibility and strength.", instructor1, "2021-03-23", "13:00", 10)
yogaclass_repository.save(yogaclass2)


pdb.set_trace()