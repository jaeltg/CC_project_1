from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.yogaclass import YogaClass
import repositories.yogaclass_repository as yogaclass_repository

yogaclasses_blueprint = Blueprint("yogaclasses", __name__)