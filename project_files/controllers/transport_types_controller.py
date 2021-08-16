from flask import Flask, request, redirect, render_template, Blueprint

from models.transport import Transport
import repositories.transport_repository as transport_repo

transport_blueprint = Blueprint("transport_types", __name__)

# Index (all the purposes on one screen)

@transport_blueprint.route("/transport_types")
def transport_types():
    transport_types = transport_repo.select_all()
    return render_template("transport_types/index.html", transport_types = transport_types)

# New (add a new purpose screen)


# Create (posting the new purpose to the list)



# Edit Later if needed



# Update Later if needed



# Delete Later if needed
