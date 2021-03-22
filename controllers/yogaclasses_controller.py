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