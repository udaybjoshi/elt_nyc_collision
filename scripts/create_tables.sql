CREATE TABLE source_collision_data (
    collision_id BIGINT PRIMARY KEY,         -- Unique identifier for each collision
    crash_date DATETIME NOT NULL,            -- Date and time of the crash
    crash_time TIME NOT NULL,                -- Time of the crash
    borough VARCHAR(50),                     -- Borough where the crash occurred
    zip_code VARCHAR(10),                    -- ZIP code of the crash location
    latitude DECIMAL(9,6),                   -- Latitude of the crash location
    longitude DECIMAL(9,6),                  -- Longitude of the crash location
    location POINT GENERATED ALWAYS AS (ST_GeomFromText(CONCAT('POINT(', longitude, ' ', latitude, ')'))) STORED,                          -- Spatial point of latitude and longitude
    on_street_name VARCHAR(255),             -- Name of the street where the crash occurred
    cross_street_name VARCHAR(255),          -- Name of the cross street
    off_street_name VARCHAR(255),            -- Name of the off-street location
    number_of_persons_injured INT,           -- Number of people injured
    number_of_persons_killed INT,            -- Number of people killed
    number_of_pedestrians_injured INT,       -- Number of pedestrians injured
    number_of_pedestrians_killed INT,        -- Number of pedestrians killed
    number_of_cyclist_injured INT,           -- Number of cyclists injured
    number_of_cyclist_killed INT,            -- Number of cyclists killed
    number_of_motorist_injured INT,          -- Number of motorists injured
    number_of_motorist_killed INT,           -- Number of motorists killed
    contributing_factor_vehicle_1 VARCHAR(255), -- Contributing factor for vehicle 1
    contributing_factor_vehicle_2 VARCHAR(255), -- Contributing factor for vehicle 2
    vehicle_type_code1 VARCHAR(50),          -- Vehicle type for vehicle 1
    vehicle_type_code2 VARCHAR(50)           -- Vehicle type for vehicle 2
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

