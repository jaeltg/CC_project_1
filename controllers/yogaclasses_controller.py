from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.yogaclass import YogaClass

import repositories.yogaclass_repository as yogaclass_repository
import repositories.instructor_repository as instructor_repository

yogaclasses_blueprint = Blueprint("yogaclasses", __name__)

@yogaclasses_blueprint.route('/yogaclasses')
def yogaclass():
    yogaclasses = yogaclass_repository.select_all()
    for yogaclass in yogaclasses:
        members = yogaclass_repository.members(yogaclass)
        yogaclass.check_if_capacity(members)
    return render_template("yogaclasses/index.html", title = "Classes", all_yogaclasses=yogaclasses)

@yogaclasses_blueprint.route('/yogaclasses/<id>')
def show_yogaclass(id):
    yogaclass = yogaclass_repository.select(id)
    members = yogaclass_repository.members(yogaclass)
    member_count = yogaclass.count_members(members)
    bookings = yogaclass_repository.bookings(yogaclass)
    return render_template("yogaclasses/show.html", title=yogaclass.name, selected_yogaclass = yogaclass, found_members = members, found_bookings = bookings, member_count=member_count)

@yogaclasses_blueprint.route('/yogaclasses/new')
def new_yogaclass():
    instructors = instructor_repository.select_all()
    return render_template("yogaclasses/new.html", title="Add Class", all_instructors = instructors)

@yogaclasses_blueprint.route('/yogaclasses', methods=['POST'])
def create_yogaclass():
    name = request.form["name"]
    duration = request.form["duration"]
    description = request.form["description"]
    instructor_id = request.form["instructor"]
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]

    instructor = instructor_repository.select(instructor_id)

    yogaclass = YogaClass(name, duration, description, instructor, date, time, capacity)

    yogaclass_repository.save(yogaclass)

    return redirect('/yogaclasses')    

@yogaclasses_blueprint.route('/yogaclasses/<id>/edit', methods =['GET'])
def edit_yogaclass(id):
    yogaclass = yogaclass_repository.select(id)
    instructors = instructor_repository.select_all()
    return render_template('yogaclasses/edit.html', title = "Edit Class", selected_yogaclass = yogaclass, all_instructors = instructors)

@yogaclasses_blueprint.route("/yogaclasses/<id>", methods=['POST'])
def update_yogaclass(id):
    name = request.form["name"]
    duration = request.form["duration"]
    description = request.form["description"]
    instructor_id = request.form["instructor"]
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    active = request.form["active"]

    instructor = instructor_repository.select(instructor_id)

    yogaclass = YogaClass(name, duration, description, instructor, date, time, capacity, active, id)

    yogaclass_repository.update(yogaclass)
    return redirect(f'/yogaclasses/{id}')

@yogaclasses_blueprint.route("/yogaclasses/<id>/delete", methods=['POST'])
def delete_yogaclass(id):
    yogaclass_repository.delete(id)
    return redirect('/yogaclasses')    
