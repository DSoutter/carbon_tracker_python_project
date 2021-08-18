from flask import Flask, request, redirect, render_template, Blueprint

from models.transport import Transport
import repositories.transport_repository as transport_repo

from models.trip import Trip
import repositories.trip_repository as trip_repo

transport_blueprint = Blueprint("transport_types", __name__)

# Index (all the types on one screen)

@transport_blueprint.route("/transport_types")
def transport_types():
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    count_of_trips = trip_repo.count()
    transport_types = transport_repo.select_all()
    return render_template("transport_types/index.html", transport_types = transport_types, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees)

# New (add a new type screen)

@transport_blueprint.route("/transport_types/new")
def transport_type():
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    count_of_trips = trip_repo.count()
    return render_template("transport_types/new.html", total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees)

# Create (posting the new type to the list)

@transport_blueprint.route("/transport_types", methods=['POST'])
def create_transport_type():
    transport_type = request.form["transport_type"]
    transport_mpg = request.form["transport_mpg"]
    new_type = Transport(transport_type, int(transport_mpg))
    transport_repo.save(new_type)
    return redirect("/transport_types")

# Edit Later if needed

@transport_blueprint.route("/transport_types/edit/<id>")
def edit_transport_type(id):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    count_of_trips = trip_repo.count()
    transport_type = transport_repo.select(id)
    return render_template('transport_types/edit.html', transport_type=transport_type, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees)

# Update Later if needed

@transport_blueprint.route("/transport_types/<id>", methods=['POST'])
def update_transport(id):
    mode_of_travel = request.form['transport_type']
    mpg = request.form['transport_mpg']
    transport= Transport(mode_of_travel, int(mpg), id)
    transport_repo.update(transport)
    trip_repo.update_carbon()
    return redirect("/transport_types")

# # Delete Later if needed

@transport_blueprint.route("/transport_types/delete/<id>", methods = ['POST'])
def delete_transport_type(id):
    transport_repo.delete(id)
    return redirect("/transport_types")