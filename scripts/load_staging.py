import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection details from .env file
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_to_db():
    """
    Establish a connection to the MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Database connection successful.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise

def preprocess_data(data, columns):
    """
    Preprocess data for MySQL compatibility:
    - Ensures all required columns are present.
    - Replaces NaN or empty strings with None.
    - Converts data to Python native types.

    Parameters:
        data (pd.DataFrame): The raw data.
        columns (list): The list of expected columns.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    # Add missing columns with default value None
    for column in columns:
        if column not in data.columns:
            print(f"Column '{column}' missing in data. Adding it with default value None.")
            data[column] = None

    # Ensure the DataFrame's columns match the table schema order
    data = data[columns]

    # Replace NaN and empty strings with None
    data = data.where(pd.notnull(data), None)

    # Convert all values to Python native types
    data = data.astype(object).where(pd.notnull(data), None)

    # Debug: Print a sample of the processed data
    print("Preprocessed Data Sample:")
    print(data.head())

    return data

def load_data_to_staging(csv_file_path, table_name):
    """
    Load data from a CSV file into a MySQL staging table.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the data.
        table_name (str): The name of the staging database table to insert data into.
    """
    # Columns expected in the staging table
    columns = [
        'collision_id', 'crash_date', 'crash_time', 'borough', 'zip_code',
        'latitude', 'longitude', 'on_street_name', 'cross_street_name',
        'off_street_name', 'number_of_persons_injured', 'number_of_persons_killed',
        'number_of_pedestrians_injured', 'number_of_pedestrians_killed',
        'number_of_cyclist_injured', 'number_of_cyclist_killed',
        'number_of_motorist_injured', 'number_of_motorist_killed',
        'contributing_factor_vehicle_1', 'contributing_factor_vehicle_2',
        'vehicle_type_code1', 'vehicle_type_code2'
    ]

    # Read the CSV file
    csv_file_path = ("../data/output/cleaned_api_data.csv")
    data = pd.read_csv(csv_file_path)

    # Preprocess the data
    data = preprocess_data(data, columns)

    # Establish a database connection
    connection = connect_to_db()
    cursor = connection.cursor()

    # Prepare the SQL INSERT statement dynamically
    insert_query = f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES ({', '.join(['%s'] * len(columns))})
    """

    # Insert rows into the database
    for _, row in data.iterrows():
        cursor.execute(insert_query, tuple(row))

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Data successfully loaded into table {table_name}.")

# Example usage
if __name__ == "__main__":
    csv_file_path = "../data/output/cleaned_api_data.csv"  # Adjust path as necessary
    table_name = "staging_collision_data"
    load_data_to_staging(csv_file_path, table_name)


