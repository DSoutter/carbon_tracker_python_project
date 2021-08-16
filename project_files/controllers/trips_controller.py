import re
from flask.templating import DispatchingJinjaLoader
from controllers.transport_types_controller import transport_type
from flask import Flask, request, redirect, render_template, Blueprint

from models.trip import Trip
from models.transport import Transport
from models.purpose import Purpose

import repositories.trip_repository as trip_repo
import repositories.transport_repository as transport_repo
import repositories.purpose_repository as purpose_repo

trip_blueprint = Blueprint("trips", __name__)

# Index (all the trips on one screen)

@trip_blueprint.route("/trips")
def trips():
    trips = trip_repo.select_all()
    return render_template("trips/index.html", trips = trips)

# New (add a new trip screen)

@trip_blueprint.route("/trips/new")
def new_trip():
    purposes = purpose_repo.select_all()
    transport_types = transport_repo.select_all()
    return render_template("trips/new.html", purposes = purposes, transport_types = transport_types)


# Create (posting the new trip to the list)

@trip_blueprint.route("/trips", methods=["POST"])
def create_trip():
    distance = request.form['distance']
    date = request.form['date']
    purpose_id = request.form['purpose_id']
    transport_type_id = request.form['transport_id']
    purpose = purpose_repo.select(purpose_id)
    transport_type = transport_repo.select(transport_type_id)
    new_trip = Trip(int(distance), date, purpose, transport_type)
    trip_repo.save(new_trip)
    return redirect("/trips")

# Edit Later if needed

@trip_blueprint.route("/trips/edit/<id>")
def edit_trip(id):
    purposes = purpose_repo.select_all()
    transport_types =transport_repo.select_all() 
    # purpose = purpose_repo.select(id)
    # transport_type = transport_repo.select(id)
    trip = trip_repo.select(id)
    return render_template('trips/edit.html', trip = trip, transport_type = transport_type, purposes = purposes, transport_types = transport_types)
# Update Later if needed

@trip_blueprint.route("/trips/<id>", methods=['POST'])
def update_trip(id):
    distance = request.form['distance']
    date = request.form['date']
    purpose_id = request.form["purpose_id"]
    transport_type_id = request.form["transport_id"]
    trip= Trip(distance, date, purpose_id, transport_type_id, id)
    trip_repo.update(trip)
    return redirect("/trips")

# @bitings_blueprint.route("/bitings/<id>", methods=["POST"])
# def update_biting(id):
#     human_id = request.form["human_id"]
#     zombie_id = request.form["zombie_id"]
#     human = human_repository.select(human_id)
#     zombie = zombie_repository.select(zombie_id)
#     biting = Biting(human, zombie, id)
#     biting_repository.update(biting)
#     return redirect("/bitings")

# Delete Later if needed