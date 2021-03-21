import pdb
from models.yogaclass import YogaClass
from models.member import Member
from models.booking import Booking

import repositories.yogaclass_repository as yogaclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

yogaclass_repository.delete_all()
member_repository.delete_all()

member1 = Member("Jessica Day", "13/02/1982", 6540003, "Standard", "The Loft, LA", "07911 123444")
member_repository.save(member1)

member2 = Member("Nick Miller", "29/09/1990", 7800643, "Standard", "The Loft, LA", "07912 123456")
member_repository.save(member2)

yogaclass1 = YogaClass("Aerial Yoga", 45, "Yoga whle being supported by a hammock to help with deeper stretches and greater flexibility.","Coach", "18:00", 10)
yogaclass_repository.save(yogaclass1)

yogaclass2 = YogaClass("Power Yoga", 45, "Fast paced class focussing  more on core and upper body work to increase stamina, flexibility and strength.", "Coach", "13:00", 10)
yogaclass_repository.save(yogaclass2)

# member_repository.delete(member1.id)
# yogaclass_repository.delete(yogaclass1.id)

# member2.test_update()
# member_repository.update(member2)

# yogaclass2.test_update()
# yogaclass_repository.update(yogaclass2)

pdb.set_trace()