import pandas as pd
import numpy as np

# Load raw data
data = pd.read_csv("data/input/raw_api_data.csv")

# Drop irrelevant columns
columns_to_keep = [
    'collision_id', 'crash_date', 'crash_time', 'borough', 'zip_code',
    'latitude', 'longitude', 'on_street_name', 'cross_street_name',
    'off_street_name', 'number_of_persons_injured', 'number_of_persons_killed',
    'number_of_pedestrians_injured', 'number_of_pedestrians_killed',
    'number_of_cyclist_injured', 'number_of_cyclist_killed',
    'number_of_motorist_injured', 'number_of_motorist_killed',
    'contributing_factor_vehicle_1', 'contributing_factor_vehicle_2',
    'vehicle_type_code1', 'vehicle_type_code2'
]
data = data[columns_to_keep]

# Handle missing data
data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')
data.dropna(subset=['latitude', 'longitude', 'crash_date'], inplace=True)

# Standardize text fields
# Remove any leading/trailing spaces and replace multiple spaces with a single space
text_fields = [
    'borough', 'on_street_name', 'cross_street_name', 'off_street_name',
    'contributing_factor_vehicle_1', 'contributing_factor_vehicle_2',
    'vehicle_type_code1', 'vehicle_type_code2'
]

for field in text_fields:
    data[field] = data[field].astype(str).str.strip()  # Remove leading/trailing spaces
    data[field] = data[field].str.replace(r'\s+', ' ', regex=True)  # Replace multiple spaces with one
    data[field] = data[field].replace('nan', None)  # Handle string 'nan' as None for consistency

# Deduplicate
data.drop_duplicates(subset=['collision_id'], inplace=True)

# Save cleaned data
output_file_path = "data/output/cleaned_api_data.csv"
data.to_csv(output_file_path, index=False)

# Print success message
print(f"Cleaned CSV loaded to output folder: {output_file_path}")


