class Booking:

    def __init__(self, member, yogaclass, id = None, available = True):
        self.member = member
        self.yogaclass = yogaclass
        self.id = id
        self.available = available

    def check_if_capacity(self, members):
        member_count = self.yogaclass.count_members(members)
        if member_count == self.yogaclass.capacity:
           self.available = False
        