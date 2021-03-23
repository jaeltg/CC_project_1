from db.run_sql import run_sql

from models.memb_type import MembType

def save(memb_type):
    sql = """
        INSERT INTO memb_types name
            VALUES %s RETURNING *
        """
    values = [memb_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    memb_type.id = id
    return memb_type

    
def select_all():
    memb_types = []

    sql = "SELECT * FROM memb_types"
    results = run_sql(sql)

    for row in results:
        memb_type = MembType(row['name'],   
                             row['id'])
        memb_types.append(memb_type)
    return memb_types


def select(id):
    memb_type = None
    sql = "SELECT * FROM memb_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        memb_type = MembType(result['name'],  
                             result['id'])
    return memb_type


def delete_all():
    sql = "DELETE FROM memb_types"
    run_sql(sql)   


def delete(id):
    sql = "DELETE FROM memb_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def update(memb_type):
    sql = """
        UPDATE memb_types 
        SET name = %s
        WHERE id = %s
        """
    values = [memb_type.name, 
              memb_type.id]
              
    run_sql(sql, values)