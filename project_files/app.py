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
    total_carbon_emissions = trip_repo.total()[0]
    amount_of_trees = trip_repo.total()[1]
    count_of_trips = trip_repo.count()
    return render_template('index.html', total_carbon_emissions= total_carbon_emissions, count_of_trips=count_of_trips, amount_of_trees=amount_of_trees)

if __name__ == '__main__':
    app.run()
