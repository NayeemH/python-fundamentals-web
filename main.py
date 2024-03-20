from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    service = db.Column(db.String(50), nullable = False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/book', methods =['POST'])
def book():
    name = request.form.get('name')
    service = request.form.get('service')

    booking = Booking (name=name, service=service)
    db.session.add(booking)
    db.session.commit()
    return redirect(url_for('bookings'))

@app.route('/bookings') # to show all bookings details
def bookings():
    all_bookings = Booking.query.all()
    return render_template('bookings.html', bookings=all_bookings)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create database tables before running the app
    app.run(debug=True)


