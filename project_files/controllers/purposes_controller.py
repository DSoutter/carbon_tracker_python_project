from flask import Flask, request, redirect, render_template, Blueprint

from models.purpose import Purpose
import repositories.purpose_repository as purpose_repo

purposes_blueprint = Blueprint("purposes", __name__)

# Index (all the purposes on one screen)

@purposes_blueprint.route("/purposes")
def purposes():
    purposes = purpose_repo.select_all()
    return render_template("humans/index.html", purposes = purposes)

# New (add a new purpose screen)



# Create (posting the new purpose to the list)



# Edit (editing an existing purpose)



# Update Later if needed



# Delete Later if needed