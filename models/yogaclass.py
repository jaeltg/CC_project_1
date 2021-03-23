class YogaClass:

   def __init__(self, name, duration, description, instructor, date, time, capacity, active = True, id = None, members = [], available = True):
        self.name = name
        self.duration = duration
        self.description = description
        self.instructor = instructor
        self.date = date
        self.time = time
        self.capacity = capacity
        self.active = active
        self.id = id
        self.members = members
        self.available = available

   def count_members(self, members):
      self.members = members
      member_count = len(self.members)
      return member_count

   def check_if_capacity(self, members):
        member_count = self.count_members(members)
        if member_count == self.capacity:
           self.available = False   

     



