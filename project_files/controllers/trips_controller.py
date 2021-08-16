from flask import Flask, request, redirect, render_template, Blueprint

from models.trip import Trip
from models.transport import Transport
from models.purpose import Purpose

import repositories.trip_repository as trip_repo
import repositories.transport_repository as transport_repo
import repositories.purpose_repository as purpose_repo

trip_blueprint = Blueprint("trips", __name__)
