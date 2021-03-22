from db.run_sql import run_sql

from models.yogaclass import YogaClass
from models.member import Member
from models.booking import Booking

import repositories.member_repository as member_repository

def save(yogaclass):
    sql = """
        INSERT INTO yogaclasses (name, 
                                duration, 
                                description,
                                instructor, 
                                time, 
                                capacity, 
                                active) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *
        """
    values = [yogaclass.name, 
              yogaclass.duration, 
              yogaclass.description, 
              yogaclass.instructor, 
              yogaclass.time, 
              yogaclass.capacity,
              yogaclass.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    yogaclass.id = id
    return yogaclass


def select_all():
    yogaclasses = []

    sql = "SELECT * FROM yogaclasses"
    results = run_sql(sql)

    for row in results:
        yogaclass = YogaClass(row['name'], 
                              row['duration'],
                              row['description'],
                              row['instructor'], 
                              row['time'], 
                              row['capacity'], 
                              row['active'],   
                              row['id'])
        yogaclasses.append(yogaclass)
    return yogaclasses


def select(id):
    yogaclass = None
    sql = "SELECT * FROM yogaclasses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        yogaclass = YogaClass(result['name'], 
                              result['duration'],
                              result['description'],
                              result['instructor'], 
                              result['time'], 
                              result['capacity'], 
                              result['active'],   
                              result['id'])
    return yogaclass


def delete_all():
    sql = "DELETE FROM yogaclasses"
    run_sql(sql) 


def delete(id):
    sql = "DELETE FROM yogaclasses WHERE id = %s"
    values = [id]
    run_sql(sql, values)    


def update(yogaclass):
    sql = """
        UPDATE yogaclasses 
        SET (name, 
            duration, 
            description,
            instructor, 
            time, 
            capacity, 
            active)  
             = (%s, %s, %s, %s, %s, %s, %s) 
             WHERE id = %s
        """
    values = [yogaclass.name, 
              yogaclass.duration, 
              yogaclass.description, 
              yogaclass.instructor, 
              yogaclass.time, 
              yogaclass.capacity,
              yogaclass.active,
              yogaclass.id]
    run_sql(sql, values) 

def members(yogaclass):
    sql = """
        SELECT members.* FROM members
        INNER JOIN bookings
        ON members.id = bookings.member_id
        WHERE yogaclass_id = %s
     """
    values = [yogaclass.id]
    results = run_sql(sql, values)
    members = []
    for row in results:
       member = Member(row['name'], 
                       row['date_of_birth'],
                       row['memb_number'],
                       row['memb_type'], 
                       row['address'], 
                       row['contact_number'], 
                       row['active'],   
                       row['id'])
       members.append(member)
    return members      

def bookings(yogaclass):
    sql = """
        SELECT * FROM bookings
        WHERE yogaclass_id = %s
     """
    values = [yogaclass.id]
    results = run_sql(sql, values)
    bookings = []
    for row in results:
        member = member_repository.select(row['member_id'])
        yogaclass = select(row['yogaclass_id'])
        booking = Booking(member, yogaclass, row['id'])
        bookings.append(booking)
    return bookings    
