from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.member import Member

import repositories.member_repository as member_repository
import repositories.memb_type_repository as memb_type_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", title = "Members", all_members=members)    

@members_blueprint.route('/members/<id>')
def show_member(id):
    member = member_repository.select(id)
    yogaclasses = member_repository.yogaclasses(member)
    return render_template("members/show.html", title=member.name, selected_member= member, found_yogaclasses=yogaclasses)

@members_blueprint.route('/members/new')
def new_member():
    memb_types = memb_type_repository.select_all()
    return render_template("members/new.html", title="Add Member", all_memb_types=memb_types)

@members_blueprint.route('/members', methods=['POST'])
def create_member():
    image_url = request.form["image_url"]
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    memb_number = request.form["memb_number"]
    memb_type_id = request.form["memb_type"]
    address = request.form["address"]
    contact_number = request.form["contact_number"]

    memb_type = memb_type_repository.select(memb_type_id)

    member = Member(image_url, name, date_of_birth, memb_number, memb_type, address, contact_number)

    member_repository.save(member)

    return redirect('/members')

@members_blueprint.route('/members/<id>/edit', methods =['GET'])
def edit_member(id):
    member = member_repository.select(id)
    memb_types = memb_type_repository.select_all()
    return render_template('members/edit.html', title = "Edit Member", selected_member = member, all_memb_types = memb_types)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update_member(id):
    image_url = request.form["image_url"]
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    memb_number = request.form["memb_number"]
    memb_type_id = request.form["memb_type"]
    address = request.form["address"]
    contact_number = request.form["contact_number"]
    active = request.form["active"]

    memb_type = memb_type_repository.select(memb_type_id)

    member = Member(image_url, name, date_of_birth, memb_number, memb_type, address, contact_number, active, id)

    member_repository.update(member)
    return redirect(f'/members/{id}')

@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')


