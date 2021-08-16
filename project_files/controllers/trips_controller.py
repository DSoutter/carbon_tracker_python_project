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



# Create (posting the new trip to the list)



# Edit Later if needed



# Update Later if needed



# Delete Later if needed