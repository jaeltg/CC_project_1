from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", title = "Members", all_members=members)    

@members_blueprint.route('/members/<id>')
def show_member(id):
    member = member_repository.select(id)
    return render_template("members/show.html", title=member.name, selected_member= member)

@members_blueprint.route('/members/new')
def new_member():
    return render_template("members/new.html", title="Add Member")

@members_blueprint.route('/members', methods=['POST'])
def create_task():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    memb_number = request.form["memb_number"]
    memb_type = request.form["memb_type"]
    address = request.form["address"]
    contact_number = request.form["contact_number"]

    member = Member(name, date_of_birth, memb_number, memb_type, address, contact_number)

    member_repository.save(member)

    return redirect('/members')

@members_blueprint.route('/members/<id>/edit', methods =['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', title = "Edit Member", selected_member = member)