from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

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
    return f"Thank you, {name}, for booking {service}!"

if __name__ == '__main__':
    app.run(debug=True)


