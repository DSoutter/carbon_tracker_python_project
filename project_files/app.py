from flask import Flask, render_template

from controllers.purposes_controller import purposes_blueprint
from controllers.transport_types_controller import transport_blueprint
from controllers.trips_controller import trip_blueprint

app = Flask(__name__)

app.register_blueprint(purposes_blueprint)
app.register_blueprint(transport_blueprint)
app.register_blueprint(trip_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
