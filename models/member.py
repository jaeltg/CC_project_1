class Member:

    def __init__(self, name, date_of_birth, memb_number, memb_type, address, contact_number, active = True, id = None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.memb_number = memb_number
        self.memb_type = memb_type
        self.address = address
        self.contact_number = contact_number
        self.active = active
        self.id = id 