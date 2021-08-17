from flask.templating import DispatchingJinjaLoader

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
    trip = trip_repo.select(id)
    return render_template('trips/edit.html', trip = trip, purposes = purposes, transport_types = transport_types)

# Update Later if needed

@trip_blueprint.route("/trips/<id>", methods=['POST'])
def update_trip(id):
    distance = request.form['distance']
    date = request.form['date']
    purpose_id = request.form["purpose_id"]
    transport_type_id = request.form["transport_type_id"]
    purpose = purpose_repo.select(purpose_id)
    transport_type = transport_repo.select(transport_type_id)
    trip= Trip(distance, date, purpose, transport_type, id)
    trip_repo.update(trip)
    return redirect("/trips")

# Delete Later if needed

@trip_blueprint.route("/trips/delete/<id>", methods=["POST"])
def delete_trip(id):
    trip_repo.delete(id)
    return redirect("/trips")