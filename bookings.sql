CREATE DATABASE hotel_booking_system;

USE hotel_booking_system;

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    room_type VARCHAR(30),
    check_in DATE,
    check_out DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some example data
INSERT INTO
    bookings (
        customer_name,
        email,
        phone_number,
        room_type,
        check_in,
        check_out
    )
VALUES (
        'John Doe',
        'johndoe@example.com',
        '1234567890',
        'single',
        '2024-09-20',
        '2024-09-25'
    ),
    (
        'Jane Smith',
        'janesmith@example.com',
        '0987654321',
        'suite',
        '2024-09-22',
        '2024-09-28'
    );