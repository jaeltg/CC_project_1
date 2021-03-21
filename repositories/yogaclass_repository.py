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