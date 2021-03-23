from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.yogaclass_repository as yogaclass_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings/successful")
def booking_successful():
    return render_template("bookings/successful.html", title="Booking Succesful!")

@bookings_blueprint.route("/bookings/unsuccessful")
def booking_unsuccessful():
    return render_template("bookings/unsuccessful.html", title="Class is Full!")

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    yogaclasses = yogaclass_repository.select_all()
    return render_template("bookings/new.html", title="Make a Booking", all_members = members, all_yogaclasses = yogaclasses)

@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    member_id = request.form['member_id']
    yogaclass_id = request.form['yogaclass_id']
    member = member_repository.select(member_id)
    yogaclass = yogaclass_repository.select(yogaclass_id)
    members = yogaclass_repository.members(yogaclass)
    booking = Booking(member, yogaclass)
    booking.check_if_capacity(members)
    if booking.yogaclass.available == True:
        booking_repository.save(booking)
        return redirect('/bookings/successful')
    else:
        return redirect('/bookings/unsuccessful')    
    
@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    yogaclass_id = booking_repository.select(id).yogaclass.id
    booking_repository.delete(id)
    return redirect(f'/yogaclasses/{yogaclass_id}')

# @bookings_blueprint.route("/bookings/<id>/edit", methods=['GET'])
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template('tasks/edit.html', selected_task = task, all_users = users)

# @bookings_blueprint.route("/tasks/<id>", methods=['POST'])
# def update_task(id):
#     description = request.form['description']
#     user_id = request.form['user']
#     duration = request.form['duration']
#     completed = request.form['completed']
#     user = user_repository.select(user_id)
#     task = Task(description, user, duration, completed, id) 
#     task_repository.update(task)
#     return redirect('/tasks')        