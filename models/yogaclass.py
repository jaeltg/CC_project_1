class YogaClass:

   def __init__(self, name, duration, description, instructor, date, time, capacity, active = True, id = None, members = []):
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

   def count_members(self, members):
      self.members = members
      member_count = len(self.members)
      return member_count

     



