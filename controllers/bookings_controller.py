from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.yogaclass_repository as yogaclass_repository

bookings_blueprint = Blueprint("bookings", __name__)



@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    yogaclasses = yogaclass_repository.select_all()
    return render_template("bookings/new.html", all_members = members, all_yogaclasses = yogaclasses)