from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint
from controllers.yogaclasses_controller import yogaclasses_blueprint
from controllers.members_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(yogaclasses_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)