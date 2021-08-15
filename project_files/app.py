from flask import Flask, render_template

from controllers.purposes_controller import purposes_blueprint
# from controllers.purposes_controller import purposes_blueprint
# from controllers.purposes_controller import purposes_blueprint

app = Flask(__name__)

app.register_blueprint(purposes_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
