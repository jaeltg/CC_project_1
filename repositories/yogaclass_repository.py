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