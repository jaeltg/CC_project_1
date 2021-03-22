from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.yogaclass import YogaClass
import repositories.yogaclass_repository as yogaclass_repository

yogaclasses_blueprint = Blueprint("yogaclasses", __name__)

@yogaclasses_blueprint.route('/yogaclasses')
def yogaclass():
    yogaclasses = yogaclass_repository.select_all()
    return render_template("yogaclasses/index.html", title = "Classes", all_yogaclasses=yogaclasses)

@yogaclasses_blueprint.route('/yogaclasses/<id>')
def show_yogaclass(id):
    yogaclass = yogaclass_repository.select(id)
    return render_template("yogaclasses/show.html", title=yogaclass.name, selected_yogaclass = yogaclass)

@yogaclasses_blueprint.route('/yogaclasses/new')
def new_yogaclass():
    return render_template("yogaclasses/new.html", title="Add Class")

@yogaclasses_blueprint.route('/yogaclasses', methods=['POST'])
def create_yogaclass():
    name = request.form["name"]
    duration = request.form["duration"]
    description = request.form["description"]
    instructor = request.form["instructor"]
    time = request.form["time"]
    capacity = request.form["capacity"]

    yogaclass = YogaClass(name, duration, description, instructor, time, capacity)

    yogaclass_repository.save(yogaclass)

    return redirect('/yogaclasses')    

@yogaclasses_blueprint.route('/yogaclasses/<id>/edit', methods =['GET'])
def edit_yogaclass(id):
    yogaclass = yogaclass_repository.select(id)
    return render_template('yogaclasses/edit.html', title = "Edit Class", selected_yogaclass = yogaclass)

@yogaclasses_blueprint.route("/yogaclasses/<id>", methods=['POST'])
def update_yogaclass(id):
    name = request.form["name"]
    duration = request.form["duration"]
    description = request.form["description"]
    instructor = request.form["instructor"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    active = request.form["active"]

    yogaclass = YogaClass(name, duration, description, instructor, time, capacity, active, id)

    yogaclass_repository.update(yogaclass)
    return redirect(f'/yogaclasses/{id}')
