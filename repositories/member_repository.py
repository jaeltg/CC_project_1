from db.run_sql import run_sql

from models.member import Member
from models.yogaclass import YogaClass

import repositories.instructor_repository as instructor_repository
import repositories.memb_type_repository as memb_type_repository

def save(member):
    sql = """
        INSERT INTO members (image_url,
                             name, 
                             date_of_birth, 
                             memb_number,
                             memb_type_id, 
                             address, 
                             contact_number, 
                             active) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *
        """
    values = [member.image_url,
              member.name, 
              member.date_of_birth, 
              member.memb_number, 
              member.memb_type.id, 
              member.address, 
              member.contact_number,
              member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

    
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        memb_type = memb_type_repository.select(row['memb_type_id'])
        member = Member(row['image_url'],
                        row['name'], 
                        row['date_of_birth'],
                        row['memb_number'],
                        memb_type, 
                        row['address'], 
                        row['contact_number'], 
                        row['active'],   
                        row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        memb_type = memb_type_repository.select(result['memb_type_id'])
        member = Member(result['image_url'],
                        result['name'], 
                        result['date_of_birth'],
                        result['memb_number'],
                        memb_type, 
                        result['address'], 
                        result['contact_number'], 
                        result['active'],   
                        result['id'])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)   


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(member):
    sql = """
        UPDATE members 
        SET (image_url,
             name, 
             date_of_birth, 
             memb_number,
             memb_type_id, 
             address, 
             contact_number, 
             active)  
             = (%s, %s, %s, %s, %s, %s, %s, %s) 
             WHERE id = %s
        """
    values = [member.image_url,
              member.name, 
              member.date_of_birth, 
              member.memb_number, 
              member.memb_type.id, 
              member.address, 
              member.contact_number,
              member.active,
              member.id]
    run_sql(sql, values)

def yogaclasses(member):
    sql = """
        SELECT yogaclasses.* FROM yogaclasses
        INNER JOIN bookings
        ON yogaclasses.id = bookings.yogaclass_id
        WHERE member_id = %s
     """
    values = [member.id]
    results = run_sql(sql, values)
    yogaclasses = []
    for row in results:
       instructor = instructor_repository.select(row['instructor_id']) 
       yogaclass = YogaClass(row['name'], 
                             row['duration'],
                             row['description'],
                             instructor,
                             row['date'],
                             row['time'], 
                             row['capacity'], 
                             row['active'],   
                             row['id'])
       yogaclasses.append(yogaclass)
    return yogaclasses   