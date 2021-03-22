DROP TABLE bookings;
DROP TABLE members;
DROP TABLE yogaclasses;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,  
    name VARCHAR(255),
    date_of_birth DATE,
    memb_number INT,
    memb_type VARCHAR(255),
    address VARCHAR(500),
    contact_number VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE yogaclasses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration INT,
    description TEXT,
    instructor VARCHAR(255),
    time VARCHAR(255),
    -- CHECK INTO TIME WITHOUT SECONDS
    capacity INT,
    active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    yogaclass_id INT REFERENCES yogaclasses(id) ON DELETE CASCADE
);