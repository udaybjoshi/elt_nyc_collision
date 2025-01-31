import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
log_file = os.path.join("logs", "staging_pipeline.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("STAGING_PIPELINE")

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
        logger.error(f"Database connection error: {err}", exc_info=True)
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
            logger.warning(f"Column '{column}' missing in data. Adding it with default value None.")
            data[column] = None

    # Ensure the DataFrame's columns match the table schema order
    data = data[columns]

    # Replace NaN and empty strings with None
    data = data.where(pd.notnull(data), None)

    # Convert all values to Python native types
    data = data.astype(object).where(pd.notnull(data), None)

    # Debug: Log a sample of the processed data
    logger.info(f"Preprocessed Data Sample:\n{data.head()}")

    return data


def load_data_to_staging(csv_file_path, table_name):
    """
    Load data from a CSV file into a MySQL staging table.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the data.
        table_name (str): The name of the staging database table to insert data into.
    """
    try:
        logger.info(f"Reading data from {csv_file_path}")

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
        logger.info(f"Data successfully loaded into table {table_name}.")
    
    except Exception as e:
        logger.error(f"Error loading data to staging: {e}", exc_info=True)
        raise


def run_staging():
    """
    Run the full staging data extraction and loading process.
    """
    try:
        logger.info("Starting staging data processing...")

        # Define file paths and table name
        csv_file_path = "../data/output/cleaned_api_data.csv"  # Adjust path if needed
        table_name = "staging_collision_data"

        # Run the ETL process
        load_data_to_staging(csv_file_path, table_name)

        logger.info("Staging data processing completed successfully.")
    except Exception as e:
        logger.error(f"Staging data processing failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    run_staging()



