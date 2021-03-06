from flask import Flask, request, redirect, render_template, Blueprint

from models.purpose import Purpose
import repositories.purpose_repository as purpose_repo
import repositories.trip_repository as trip_repo

purposes_blueprint = Blueprint("purposes", __name__)

# Index (all the purposes on one screen)

@purposes_blueprint.route("/purposes")
def purposes():
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()    
    purposes = purpose_repo.select_all()
    return render_template("purposes/index.html", purposes = purposes, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# New (add a new purpose screen)

@purposes_blueprint.route("/purposes/new")
def new_purpose():
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()    
    return render_template("purposes/new.html", total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# Create (posting the new purpose to the list)

@purposes_blueprint.route("/purposes", methods=["POST"])
def create_purpose():
    travel_purpose = request.form["travel_purpose"]
    new_purpose = Purpose(travel_purpose)
    purpose_repo.save(new_purpose)
    return redirect("/purposes")


# Edit Later if needed

@purposes_blueprint.route("/purposes/edit/<id>")
def edit_purpose(id):
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    total_carbon_emissions_base = trip_repo.total()[2]
    count_of_trips = trip_repo.count()
    purpose = purpose_repo.select(id)
    return render_template('purposes/edit.html', purpose=purpose, total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees, total_carbon_emissions_base=total_carbon_emissions_base)

# Update Later if needed

@purposes_blueprint.route("/purposes/<id>", methods=['POST'])
def update_purpose(id):
    travel_purpose = request.form['travel_purpose']
    purpose= Purpose(travel_purpose, id)
    purpose_repo.update(purpose)
    return redirect("/purposes")

# Delete Later if needed

@purposes_blueprint.route("/purposes/delete/<id>", methods = ['POST'])
def delete_purpose(id):
    purpose_repo.delete(id)
    return redirect("/purposes")
