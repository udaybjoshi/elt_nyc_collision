import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
import json
import logging

# Load environment variables
load_dotenv()

# Configure logging
log_file = os.path.join("logs", "source_pipeline.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("SOURCE_PIPELINE")

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
        logger.info("Database connection successful.")
        return connection
    except mysql.connector.Error as err:
        logger.error(f"Database connection error: {err}")
        raise


def preprocess_location(data):
    """
    Preprocess the 'location' field in the DataFrame.

    Parameters:
        data (pd.DataFrame): The raw data containing the 'location' field.

    Returns:
        pd.DataFrame: The DataFrame with the 'location' field split into latitude and longitude.
    """
    def extract_coordinates(location):
        if pd.isnull(location):
            return None, None
        try:
            location_json = json.loads(location)
            return location_json.get('latitude'), location_json.get('longitude')
        except (json.JSONDecodeError, KeyError):
            return None, None

    # Apply the extraction function to the 'location' column
    data[['latitude', 'longitude']] = data['location'].apply(
        lambda loc: pd.Series(extract_coordinates(loc))
    )

    # Drop the original 'location' field
    data.drop(columns=['location'], inplace=True)
    return data


def load_data_to_db(csv_file_path, table_name):
    """
    Load data from a CSV file into a MySQL database table.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the data.
        table_name (str): The name of the database table to insert data into.
    """
    try:
        logger.info(f"Reading data from {csv_file_path}")
        data = pd.read_csv(csv_file_path)

        # Replace NaN values with None for database compatibility
        data = data.where(pd.notnull(data), None)

        # Preprocess the 'location' field
        data = preprocess_location(data)

        # Establish a database connection
        connection = connect_to_db()
        cursor = connection.cursor()

        # Prepare the SQL INSERT statement
        insert_query = f"""
            INSERT INTO {table_name} (
                collision_id,
                crash_date,
                crash_time,
                borough,
                zip_code,
                latitude,
                longitude,
                on_street_name,
                cross_street_name,
                off_street_name,
                number_of_persons_injured,
                number_of_persons_killed,
                number_of_pedestrians_injured,
                number_of_pedestrians_killed,
                number_of_cyclist_injured,
                number_of_cyclist_killed,
                number_of_motorist_injured,
                number_of_motorist_killed,
                contributing_factor_vehicle_1,
                contributing_factor_vehicle_2,
                contributing_factor_vehicle_3,
                contributing_factor_vehicle_4,
                contributing_factor_vehicle_5,
                vehicle_type_code1,
                vehicle_type_code2,
                vehicle_type_code_3,
                vehicle_type_code_4,
                vehicle_type_code_5
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Iterate through the DataFrame and insert rows into the database
        for _, row in data.iterrows():
            cursor.execute(insert_query, (
                row.get('collision_id'),
                row.get('crash_date'),
                row.get('crash_time'),
                row.get('borough'),
                row.get('zip_code'),
                row.get('latitude'),
                row.get('longitude'),
                row.get('on_street_name'),
                row.get('cross_street_name'),
                row.get('off_street_name'),
                row.get('number_of_persons_injured'),
                row.get('number_of_persons_killed'),
                row.get('number_of_pedestrians_injured'),
                row.get('number_of_pedestrians_killed'),
                row.get('number_of_cyclist_injured'),
                row.get('number_of_cyclist_killed'),
                row.get('number_of_motorist_injured'),
                row.get('number_of_motorist_killed'),
                row.get('contributing_factor_vehicle_1'),
                row.get('contributing_factor_vehicle_2'),
                row.get('contributing_factor_vehicle_3'),
                row.get('contributing_factor_vehicle_4'),
                row.get('contributing_factor_vehicle_5'),
                row.get('vehicle_type_code1'),
                row.get('vehicle_type_code2'),
                row.get('vehicle_type_code_3'),
                row.get('vehicle_type_code_4'),
                row.get('vehicle_type_code_5')
            ))

        # Commit the transaction and close the connection
        connection.commit()
        cursor.close()
        connection.close()
        logger.info(f"Data successfully loaded into table {table_name}.")
    
    except Exception as e:
        logger.error(f"Error loading data to database: {e}", exc_info=True)
        raise


def run_source():
    """
    Run the full source data extraction and loading process.
    """
    try:
        logger.info("Starting source data processing...")

        # Define file paths and table name
        csv_file_path = "./data/input/raw_api_data.csv"
        table_name = "source_collision_data"

        # Run the ETL process
        load_data_to_db(csv_file_path, table_name)

        logger.info("Source data processing completed successfully.")
    except Exception as e:
        logger.error(f"Source data processing failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    run_source()



