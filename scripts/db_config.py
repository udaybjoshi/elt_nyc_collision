import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def get_db_connection():
    """
    Establish a connection to the MySQL database.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection: A connection object to interact with the database.

    Raises:
        mysql.connector.Error: If the connection fails.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT', 3306)),  # Default MySQL port is 3306
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise

# Example usage
if __name__ == "__main__":
    # Test the connection
    try:
        conn = get_db_connection()
        print("Connection to MySQL database was successful!")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
