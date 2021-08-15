-- Ordering matters, ones with references to others first (trips).
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS transport_types;
DROP TABLE IF EXISTS purposes;

CREATE TABLE purposes (
    id SERIAL PRIMARY KEY,
    travel_purpose VARCHAR(255)
);

CREATE TABLE transport_types (
    id SERIAL PRIMARY KEY,
    mode_of_travel VARCHAR(255),
    carbon_per_mile INT,
    mpg INT
);

CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    distance INT,
    carbon INT,
    date DATE, 
    purpose_id SERIAL REFERENCES purposes(id),
    transport_type_id SERIAL REFERENCES transport_types(id)
);
