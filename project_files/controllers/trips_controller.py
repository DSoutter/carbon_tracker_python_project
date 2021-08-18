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
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips = trip_repo.select_all()
    return render_template("trips/index.html", trips = trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# New (add a new trip screen)

@trip_blueprint.route("/trips/new")
def new_trip():
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    purposes = purpose_repo.select_all()
    transport_types = transport_repo.select_all()
    return render_template("trips/new.html", purposes = purposes, transport_types = transport_types, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)


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
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    purposes = purpose_repo.select_all()
    transport_types =transport_repo.select_all() 
    trip = trip_repo.select(id)
    return render_template('trips/edit.html', trip = trip, purposes = purposes, transport_types = transport_types, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# Update Later if needed

@trip_blueprint.route("/trips/<id>", methods=['POST'])
def update_trip(id):
    distance = request.form['distance']
    date = request.form['date']
    purpose_id = request.form["purpose_id"]
    transport_type_id = request.form["transport_type_id"]
    purpose = purpose_repo.select(purpose_id)
    transport_type = transport_repo.select(transport_type_id)
    trip= Trip(int(distance), date, purpose, transport_type, id)
    trip_repo.update(trip)
    return redirect("/trips")

# Delete Later if needed

@trip_blueprint.route("/trips/delete/<id>", methods=["POST"])
def delete_trip(id):
    trip_repo.delete(id)
    return redirect("/trips")

# Year function:

@trip_blueprint.route("/trips/year/<year>")
def trips_by_year(year):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips = trip_repo.select_all_by_year(year)
    return render_template("trips/index.html", trips = trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# Month function:

@trip_blueprint.route("/trips/<year>/<month>")
def trips_by_month(month, year):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips = trip_repo.select_all_by_month(month, year)
    return render_template("trips/index.html", trips = trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# Day function: 

@trip_blueprint.route("/trips/<year>/<month>/<day>")
def trips_by_day(day, month, year):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips = trip_repo.select_all_by_day(day, month, year)
    return render_template("trips/index.html", trips = trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# purposes list function:
@trip_blueprint.route("/trips/purpose/<id>")
def trips_purposes_by_id(id):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips= trip_repo.select_all_by_purpose(id)
    return render_template("trips/index.html", trips=trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# journey by function:
@trip_blueprint.route("/trips/mode/<id>")
def trips_by_mode(id):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    trips = trip_repo.select_all_by_mode(id)
    return render_template("trips/index.html", trips = trips, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)