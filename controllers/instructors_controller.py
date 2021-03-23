from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)

@instructors_blueprint.route('/instructors')
def instructors():
    instructors = instructor_repository.select_all()
    return render_template("instructors/index.html", title = "Instructors", all_instructors=instructors)    

@instructors_blueprint.route('/instructors/new')
def new_instructor():
    return render_template("instructors/new.html", title="Add Instructor")

@instructors_blueprint.route('/instructors', methods=['POST'])
def create_instructor():
    name = request.form["name"]
    contact_number = request.form["contact_number"]

    instructor = Instructor(name, contact_number)

    instructor_repository.save(instructor)

    return redirect('/instructors')

@instructors_blueprint.route('/instructors/<id>/edit', methods =['GET'])
def edit_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template('instructors/edit.html', title = "Edit Instructor", selected_instructor = instructor)

@instructors_blueprint.route("/instructors/<id>", methods=['POST'])
def update_instructor(id):
    name = request.form["name"]
    contact_number = request.form["contact_number"]

    instructor = Instructor(name, contact_number, id)

    instructor_repository.update(instructor)
    return redirect('/instructors')

@instructors_blueprint.route("/instructors/<id>/delete", methods=['POST'])
def delete_instructor(id):
    instructor_repository.delete(id)
    return redirect('/instructors')