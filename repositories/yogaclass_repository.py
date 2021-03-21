from db.run_sql import run_sql

from models.yogaclass import YogaClass

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