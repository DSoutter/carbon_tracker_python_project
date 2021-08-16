from flask import Flask, render_template

from controllers.purposes_controller import purposes_blueprint
from controllers.transport_types_controller import transport_blueprint
from controllers.trips_controller import trip_blueprint
import repositories.trip_repository as trip_repo

app = Flask(__name__)

app.register_blueprint(purposes_blueprint)
app.register_blueprint(transport_blueprint)
app.register_blueprint(trip_blueprint)


@app.route("/")
def main():
    total_carbon_emissions = trip_repo.total()
    return render_template('index.html', total_carbon_emissions= total_carbon_emissions)

if __name__ == '__main__':
    app.run()
