from db.run_sql import run_sql

from models.instructor import Instructor
from models.yogaclass import YogaClass


def save(instructor):
    sql = """
        INSERT INTO instructors (name, contact_number)
            VALUES (%s, %s) RETURNING *
        """
    values = [instructor.name, instructor.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id
    return instructor

    
def select_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        instructor = Instructor(row['name'],
                                row['contact_number'],    
                                row['id'])
        instructors.append(instructor)
    return instructors


def select(id):
    instructor = None
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        instructor = Instructor(result['name'], 
                                result['contact_number'],  
                                result['id'])
    return instructor


def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)   


def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(instructor):
    sql = """
        UPDATE instructors 
        SET (name, contact_number) = (%s, %s) 
        WHERE id = %s
        """
    values = [instructor.name, 
              instructor.contact_number,
              instructor.id]
    run_sql(sql, values)

def yogaclasses(instructor):
    yogaclasses = []

    sql = "SELECT * FROM yogaclasses WHERE instructor_id = %s"
    values = [instructor.id]
    results = run_sql(sql, values)

    for row in results:
        yogaclass = YogaClass(row['name'], 
                              row['duration'],
                              row['description'],
                              row['instructor_id'],
                              row['date'],
                              row['time'], 
                              row['capacity'], 
                              row['active'],   
                              row['id'])
        yogaclasses.append(yogaclass)
    return yogaclasses    