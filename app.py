
from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL Database connection details
db_config = {
    'host': 'localhost',
    'database': 'hotel_booking_system',
    'user': 'root',  # Replace with your MySQL username
    'password': 'Security1234',  # Replace with your MySQL password
}

def get_bookings():
    """Retrieve bookings from the MySQL database."""
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    try:
        # connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            # cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM bookings")
            bookings = cursor.fetchall()
            return bookings
    except Error as e:
        print(f"Error retrieving bookings: {e}")
        return []
    finally:
        """if connection.is_connected():"""
        cursor.close()
        connection.close()

@app.route('/')
def show_bookings():
    """Render the bookings in an HTML page."""
    bookings = get_bookings()
    return render_template('bookings.html', bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)
