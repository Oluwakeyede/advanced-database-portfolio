CREATE DATABASE IF NOT EXISTS west_haven_hotel;
USE west_haven_hotel;

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE room_types (
    room_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    nightly_rate DECIMAL(10,2) NOT NULL CHECK (nightly_rate > 0),
    max_guests INT NOT NULL CHECK (max_guests > 0)
);

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type_id INT NOT NULL,
    status ENUM('Available','Occupied','Maintenance') NOT NULL DEFAULT 'Available',
    FOREIGN KEY (room_type_id) REFERENCES room_types(room_type_id)
);

CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE staff_shifts (
    shift_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT NOT NULL,
    shift_date DATE NOT NULL UNIQUE,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT NOT NULL,
    staff_id INT NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status ENUM('Reserved','Checked-in','Checked-out','Cancelled') NOT NULL DEFAULT 'Reserved',
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    CHECK (check_out_date > check_in_date)
);

CREATE TABLE booking_rooms (
    booking_room_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    room_id INT NOT NULL,
    rate_charged DECIMAL(10,2) NOT NULL CHECK (rate_charged > 0),
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    UNIQUE (booking_id, room_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
    method VARCHAR(30) NOT NULL,
    paid_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);