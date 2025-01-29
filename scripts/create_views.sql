'''
High Risk Areas View
Purpose: Identify collision hotspots based on the number of incidents in specific locations (e.g., boroughs, streets).
'''
CREATE VIEW high_risk_areas AS
SELECT 
    borough,
    on_street_name,
    COUNT(*) AS total_collisions,
    SUM(number_of_persons_injured) AS total_injuries,
    SUM(number_of_persons_killed) AS total_fatalities
FROM 
    entities_collision_data
GROUP BY 
    borough, on_street_name
HAVING 
    total_collisions > 10 -- Threshold for identifying a hotspot
ORDER BY 
    total_collisions DESC;

'''
Collision Severity Trends View
Purpose: Analyze trends in the severity of collisions over time.
'''
CREATE VIEW collision_severity_trends AS
SELECT 
    DATE(crash_date) AS collision_date,
    SUM(number_of_persons_injured) AS total_injuries,
    SUM(number_of_persons_killed) AS total_fatalities,
    COUNT(*) AS total_collisions
FROM 
    entities_collision_data
GROUP BY 
    collision_date
ORDER BY 
    collision_date ASC;

'''
Contributing Factors Analysis View
Purpose: Identify common contributing factors to collisions.
'''
CREATE VIEW contributing_factors_analysis AS
SELECT 
    contributing_factor_vehicle_1 AS contributing_factor,
    COUNT(*) AS total_collisions,
    SUM(number_of_persons_injured) AS total_injuries,
    SUM(number_of_persons_killed) AS total_fatalities
FROM 
    entities_collision_data
WHERE 
    contributing_factor_vehicle_1 IS NOT NULL
GROUP BY 
    contributing_factor
ORDER BY 
    total_collisions DESC;

'''
Cyclist and Pedestrian Safety View
Purpose: Understand pedestrian and cyclist safety concerns for infrastructure planning.
'''
CREATE VIEW cyclist_pedestrian_safety AS
SELECT 
    borough,
    SUM(number_of_pedestrians_injured) AS pedestrians_injured,
    SUM(number_of_pedestrians_killed) AS pedestrians_killed,
    SUM(number_of_cyclist_injured) AS cyclists_injured,
    SUM(number_of_cyclist_killed) AS cyclists_killed
FROM 
    entities_collision_data
GROUP BY 
    borough
HAVING 
    pedestrians_injured + cyclists_injured > 5 -- Threshold for identifying safety concerns
ORDER BY 
    pedestrians_injured DESC, cyclists_injured DESC;

'''
Time-Based Collision Patterns View
Purpose: Identify patterns related to the time of day for collisions.
'''
CREATE VIEW time_based_collision_patterns AS
SELECT 
    HOUR(crash_time) AS hour_of_day,
    COUNT(*) AS total_collisions,
    SUM(number_of_persons_injured) AS total_injuries,
    SUM(number_of_persons_killed) AS total_fatalities
FROM 
    entities_collision_data
WHERE 
    crash_time IS NOT NULL
GROUP BY 
    hour_of_day
ORDER BY 
    total_collisions DESC;

'''
Policy Effectiveness View
Purpose: Evaluate the effectiveness of existing traffic laws by borough and time.
'''
CREATE VIEW policy_effectiveness AS
SELECT 
    borough,
    DATE(crash_date) AS collision_date,
    COUNT(*) AS total_collisions,
    SUM(number_of_persons_injured) AS total_injuries,
    SUM(number_of_persons_killed) AS total_fatalities
FROM 
    entities_collision_data
GROUP BY 
    borough, collision_date
ORDER BY 
    collision_date DESC;
