from flask import Flask, request, redirect, render_template, Blueprint

from models.purpose import Purpose
import repositories.purpose_repository as purpose_repo

purposes_blueprint = Blueprint("purposes", __name__)

# Index (all the purposes on one screen)

@purposes_blueprint.route("/purposes")
def purposes():
    purposes = purpose_repo.select_all()
    return render_template("purposes/index.html", purposes = purposes)

# New (add a new purpose screen)

@purposes_blueprint.route("/purposes/new")
def new_purpose():
    return render_template("purposes/new.html")

# Create (posting the new purpose to the list)

@purposes_blueprint.route("/purposes", methods=["POST"])
def create_purpose():
    travel_purpose = request.form["travel_purpose"]
    new_purpose = Purpose(travel_purpose)
    purpose_repo.save(new_purpose)
    return redirect("/purposes")


# Edit Later if needed



# Update Later if needed



# Delete Later if needed