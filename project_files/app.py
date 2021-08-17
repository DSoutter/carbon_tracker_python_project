from flask import Flask, render_template
from flask.sessions import SecureCookieSessionInterface

from controllers.purposes_controller import purposes_blueprint
from controllers.transport_types_controller import transport_blueprint
from controllers.trips_controller import trip_blueprint
import repositories.trip_repository as trip_repo
import repositories.transport_repository as transport_repo
import repositories.purpose_repository as purpose_repo


app = Flask(__name__)

app.register_blueprint(purposes_blueprint)
app.register_blueprint(transport_blueprint)
app.register_blueprint(trip_blueprint)

@app.route("/")
def main():
    total_carbon_emissions = trip_repo.total()
    # total_emissions_kg = total_carbon_emissions_base/1000
    # total_emissions_t = total_carbon_emissions_base/1000000
    # total_carbon_emissions = str(total_carbon_emissions_base) + "g"


    count_of_trips = trip_repo.count()
    return render_template('index.html', total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips)

if __name__ == '__main__':
    app.run()
