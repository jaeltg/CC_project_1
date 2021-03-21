import pdb
from models.yogaclass import YogaClass
from models.member import Member
from models.booking import Booking

import repositories.yogaclass_repository as yogaclass_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()

member1 = Member("Jessica Day", "13/02/1982", 6540003, "Standard", "The Loft, LA", "07911 123444")
member_repository.save(member1)

member2 = Member("Nick Miller", "29/09/1990", 7800643, "Standard", "The Loft, LA", "07912 123456")
member_repository.save(member2)

# member_repository.delete(member1.id)

pdb.set_trace()