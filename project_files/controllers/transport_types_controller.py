from flask import Flask, request, redirect, render_template, Blueprint

from models.transport import Transport
import repositories.transport_repository as transport_repo

transport_blueprint = Blueprint("transport_types", __name__)

# Index (all the types on one screen)

@transport_blueprint.route("/transport_types")
def transport_types():
    transport_types = transport_repo.select_all()
    return render_template("transport_types/index.html", transport_types = transport_types)

# New (add a new type screen)


# Create (posting the new type to the list)



# Edit Later if needed



# Update Later if needed



# Delete Later if needed
