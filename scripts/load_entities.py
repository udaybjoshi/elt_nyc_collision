import mysql.connector
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Configure logging
log_file = os.path.join("logs", "entities_pipeline.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ENTITIES_PIPELINE")

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


def transfer_data_to_entities_table():
    """
    Transfer data from the staging_collision_data table to the entities_collision_data table.
    """
    transfer_query = """
        INSERT INTO entities_collision_data (
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
            vehicle_type_code1,
            vehicle_type_code2
        )
        SELECT
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
            vehicle_type_code1,
            vehicle_type_code2
        FROM staging_collision_data;
    """

    # Establish database connection
    connection = connect_to_db()
    cursor = connection.cursor()

    try:
        logger.info("Starting data transfer from staging to entities table...")
        cursor.execute(transfer_query)
        connection.commit()
        logger.info("Data successfully transferred from staging_collision_data to entities_collision_data.")
    except mysql.connector.Error as err:
        logger.error(f"Error transferring data: {err}", exc_info=True)
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


def run_entities():
    """
    Run the ETL process to transfer data from staging to entities table.
    """
    try:
        logger.info("Starting entities data processing...")
        transfer_data_to_entities_table()
        logger.info("Entities data processing completed successfully.")
    except Exception as e:
        logger.error(f"Entities data processing failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    run_entities()

