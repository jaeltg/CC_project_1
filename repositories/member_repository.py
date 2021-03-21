from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = """
        INSERT INTO members (name, 
                             date_of_birth, 
                             memb_number,
                             memb_type, 
                             address, 
                             contact_number, 
                             active) 
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *
        """
    values = [member.name, 
              member.date_of_birth, 
              member.memb_number, 
              member.memb_type, 
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


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], 
                        result['date_of_birth'],
                        result['memb_number'],
                        result['memb_type'], 
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
