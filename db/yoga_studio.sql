DROP TABLE bookings;
DROP TABLE members;
DROP TABLE yogaclasses;
DROP TABLE instructors;

CREATE TABLE memb_types (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,  
    name VARCHAR(255),
    date_of_birth DATE,
    memb_number INT,
    memb_type_id INT REFERENCES memb_types(id),
    address VARCHAR(500),
    contact_number VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_number VARCHAR(255)
);

CREATE TABLE yogaclasses (
    id SERIAL PRIMARY KEY,
    image_url TEXT,
    name VARCHAR(255),
    duration INT,
    description TEXT,
    instructor_id INT REFERENCES instructors(id) ON DELETE CASCADE,
    date DATE,
    time VARCHAR(255),
    capacity INT,
    active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    yogaclass_id INT REFERENCES yogaclasses(id) ON DELETE CASCADE
);