from db.run_sql import run_sql
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.yogaclass_repository as yogaclass_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, yogaclass_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.yogaclass.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        yogaclass = yogaclass_repository.select(row['yogaclass_id'])
        booking = Booking(member, yogaclass, row['id'])
        bookings.append(booking)
    return bookings
 