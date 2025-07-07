from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# in-memory list to store bookings
all_bookings = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        photographer_id = request.form['photographer_id']
        user_id = request.form['user_id']
        date = request.form['date']
        price = float(request.form['price'])

        booking = {
            'photographer_id': photographer_id,
            'user_id': user_id,
            'date': date,
            'price': price,
            'status': "Upcoming"
        }
        all_bookings.append(booking)
        flash("Your booking has been confirmed!", "success")
        return render_template('book.html', booking=booking, message="Booking successful!")

    return render_template('book.html')

@app.route('/booking_history')
def booking_history():
    return render_template('booking_history.html', bookings=all_bookings)

# ✅ Modified for EC2 hosting
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)