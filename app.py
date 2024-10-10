from flask import Flask
from controllers.accidents_route import bp_accident
from controllers.load_data_route import bp_load_data
app = Flask(__name__)

app.register_blueprint(bp_load_data, url_prefix='/load_data')
app.register_blueprint(bp_accident, url_prefix='/accident')
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
