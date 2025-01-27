import os
import pandas as pd

INPUT_FILE = './data/input/raw_api_data.csv'

def validate_data(file_path):
    """
    Validate the quality of data in the provided CSV file.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if all validation checks pass, False otherwise.

    Rules:
        1. The file exists and is not empty.
        2. Mandatory columns are present.
        3. No null values in mandatory columns.
        4. Logical integrity checks on numeric fields.
        5. Date columns are in a valid format.
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Validation failed: File {file_path} does not exist.")
        return False

    # Load the data
    data = pd.read_csv(file_path)

    # Rule 1: Check if the file is empty
    if data.empty:
        print("Validation failed: The file is empty.")
        return False

    # Rule 2: Mandatory columns are present
    required_columns = ['collision_id', 'crash_date', 'vehicle_type_code1', 
                        'number_of_persons_injured', 'number_of_persons_killed']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        print(f"Validation failed: Missing columns - {missing_columns}")
        return False

    # Rule 3: No null values in mandatory columns
    for col in required_columns:
        if data[col].isnull().any():
            print(f"Validation failed: Null values found in column '{col}'")
            return False

    # Rule 4: Logical integrity checks on numeric fields
    if (data['number_of_persons_injured'] < 0).any():
        print("Validation failed: Negative values in 'number_of_persons_injured'")
        return False
    if (data['number_of_persons_killed'] < 0).any():
        print("Validation failed: Negative values in 'number_of_persons_killed'")
        return False

    # Rule 5: Check if 'crash_date' is in a valid date format
    try:
        data['crash_date'] = pd.to_datetime(data['crash_date'], errors='coerce')
        if data['crash_date'].isnull().any():
            print("Validation failed: Invalid date format in 'crash_date'")
            return False
    except Exception as e:
        print(f"Validation failed: Error parsing 'crash_date': {e}")
        return False

    print("Validation passed: All checks passed successfully.")
    return True

# Example usage
if __name__ == "__main__":
    is_valid = validate_data(INPUT_FILE)
    if is_valid:
        print("Data is ready for transformation.")
    else:
        print("Data quality checks failed. Please fix the issues and try again.")
