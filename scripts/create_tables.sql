-- source table
CREATE TABLE IF NOT EXISTS source_collision_data (
	collision_id BIGINT PRIMARY KEY,     -- Unique identifier for each collision
    crash_date DATETIME,                        -- Date of the crash
    crash_time TIME,                            -- Time of the crash
    borough VARCHAR(50),                       -- Borough where the crash occurred
    zip_code VARCHAR(10),                      -- ZIP code of the crash location
    latitude DECIMAL(10, 8),                   -- Latitude of the crash location
    longitude DECIMAL(11, 8),                  -- Longitude of the crash location
    on_street_name VARCHAR(255),              -- Name of the street where the crash occurred
    cross_street_name VARCHAR(255),           -- Name of the intersecting street
    off_street_name VARCHAR(255),             -- Name of the off-street location
    number_of_persons_injured INT,            -- Number of persons injured
    number_of_persons_killed INT,             -- Number of persons killed
    number_of_pedestrians_injured INT,        -- Number of pedestrians injured
    number_of_pedestrians_killed INT,         -- Number of pedestrians killed
    number_of_cyclist_injured INT,            -- Number of cyclists injured
    number_of_cyclist_killed INT,             -- Number of cyclists killed
    number_of_motorist_injured INT,           -- Number of motorists injured
    number_of_motorist_killed INT,            -- Number of motorists killed
    contributing_factor_vehicle_1 VARCHAR(255), -- Contributing factor for vehicle 1
    contributing_factor_vehicle_2 VARCHAR(255), -- Contributing factor for vehicle 2
    contributing_factor_vehicle_3 VARCHAR(255), -- Contributing factor for vehicle 3
    contributing_factor_vehicle_4 VARCHAR(255), -- Contributing factor for vehicle 4
    contributing_factor_vehicle_5 VARCHAR(255), -- Contributing factor for vehicle 5
    vehicle_type_code1 VARCHAR(255),          -- Type of vehicle 1
    vehicle_type_code2 VARCHAR(255),          -- Type of vehicle 2
    vehicle_type_code_3 VARCHAR(255),          -- Type of vehicle 3
    vehicle_type_code_4 VARCHAR(255),          -- Type of vehicle 4
    vehicle_type_code_5 VARCHAR(255)           -- Type of vehicle 5
);

-- staging table
CREATE TABLE staging_collision_data (
    collision_id BIGINT PRIMARY KEY,                -- Unique identifier for each collision
    crash_date DATETIME NOT NULL,                   -- Date of the crash
    crash_time TIME,                                -- Time of the crash
    borough VARCHAR(50),                            -- Borough where the crash occurred
    zip_code VARCHAR(10),                           -- ZIP code of the crash location
    latitude DECIMAL(10, 7),                        -- Latitude of the crash location
    longitude DECIMAL(10, 7),                       -- Longitude of the crash location
    on_street_name VARCHAR(255),                   -- Name of the street where the crash occurred
    cross_street_name VARCHAR(255),                -- Name of the cross street
    off_street_name VARCHAR(255),                  -- Name of the off-street
    number_of_persons_injured INT DEFAULT 0,        -- Number of persons injured
    number_of_persons_killed INT DEFAULT 0,         -- Number of persons killed
    number_of_pedestrians_injured INT DEFAULT 0,    -- Number of pedestrians injured
    number_of_pedestrians_killed INT DEFAULT 0,     -- Number of pedestrians killed
    number_of_cyclist_injured INT DEFAULT 0,        -- Number of cyclists injured
    number_of_cyclist_killed INT DEFAULT 0,         -- Number of cyclists killed
    number_of_motorist_injured INT DEFAULT 0,       -- Number of motorists injured
    number_of_motorist_killed INT DEFAULT 0,        -- Number of motorists killed
    contributing_factor_vehicle_1 VARCHAR(255),     -- Contributing factor of vehicle 1
    contributing_factor_vehicle_2 VARCHAR(255),     -- Contributing factor of vehicle 2
    vehicle_type_code1 VARCHAR(255),                -- Type of vehicle 1
    vehicle_type_code2 VARCHAR(255)                 -- Type of vehicle 2
);

-- entities_collision_data
CREATE TABLE staging_collision_data (
    collision_id BIGINT PRIMARY KEY,                -- Unique identifier for each collision
    crash_date DATETIME NOT NULL,                       -- Date of the crash
    crash_time TIME,                                -- Time of the crash
    borough VARCHAR(50),                            -- Borough where the crash occurred
    zip_code VARCHAR(10),                           -- ZIP code of the crash location
    latitude DECIMAL(10, 7),                        -- Latitude of the crash location
    longitude DECIMAL(10, 7),                       -- Longitude of the crash location
    on_street_name VARCHAR(255),                   -- Name of the street where the crash occurred
    cross_street_name VARCHAR(255),                -- Name of the cross street
    off_street_name VARCHAR(255),                  -- Name of the off-street
    number_of_persons_injured INT DEFAULT 0,        -- Number of persons injured
    number_of_persons_killed INT DEFAULT 0,         -- Number of persons killed
    number_of_pedestrians_injured INT DEFAULT 0,    -- Number of pedestrians injured
    number_of_pedestrians_killed INT DEFAULT 0,     -- Number of pedestrians killed
    number_of_cyclist_injured INT DEFAULT 0,        -- Number of cyclists injured
    number_of_cyclist_killed INT DEFAULT 0,         -- Number of cyclists killed
    number_of_motorist_injured INT DEFAULT 0,       -- Number of motorists injured
    number_of_motorist_killed INT DEFAULT 0,        -- Number of motorists killed
    contributing_factor_vehicle_1 VARCHAR(255),     -- Contributing factor of vehicle 1
    contributing_factor_vehicle_2 VARCHAR(255),     -- Contributing factor of vehicle 2
    vehicle_type_code1 VARCHAR(255),                -- Type of vehicle 1
    vehicle_type_code2 VARCHAR(255)                 -- Type of vehicle 2
);



