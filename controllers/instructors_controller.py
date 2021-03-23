from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.instructors import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)

