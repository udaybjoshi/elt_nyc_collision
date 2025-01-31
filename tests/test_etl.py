import pytest
import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from dotenv import load_dotenv
from scripts.extract import extract_data_from_api  # Update with actual function
from scripts.transform import clean_data  # Update with actual function
from scripts.load_source import load_data_to_db  # Update with actual function
from scripts.analysis import fetch_data

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Create database engine for testing
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Sample API response for mocking
SAMPLE_API_RESPONSE = [{
    "collision_id": 12345,
    "crash_date": "2025-01-30",
    "crash_time": "14:30",
    "borough": "Brooklyn",
    "number_of_persons_injured": 2,
    "number_of_persons_killed": 0,
    "vehicle_type_code1": "Sedan"
}]

# Sample transformed data for validation
SAMPLE_TRANSFORMED_DATA = pd.DataFrame(SAMPLE_API_RESPONSE)

def test_database_connection():
    """Test if the database connection is established successfully."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        assert connection.is_connected()
        connection.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")


def test_extract_data():
    """Mock API call and check if data extraction works."""
    data = extract_data_from_api("mock_url")  # Replace with actual API function
    assert isinstance(data, list)
    assert len(data) > 0
    assert "collision_id" in data[0]


def test_data_cleaning():
    """Test data transformation step."""
    cleaned_data = clean_data(SAMPLE_TRANSFORMED_DATA)
    assert "collision_id" in cleaned_data.columns
    assert cleaned_data["borough"].str.contains(" ").sum() == 0  # Ensure no leading/trailing spaces


def test_data_loading():
    """Test data loading into the database."""
    try:
        load_data_to_db("data/input/raw_api_data.csv", "staging_collision_data")
        query = "SELECT COUNT(*) FROM staging_collision_data;"
        result = fetch_data(query)
        assert result.iloc[0, 0] > 0  # Ensure data is loaded
    except Exception as e:
        pytest.fail(f"Data loading test failed: {e}")


def test_visualization_queries():
    """Test if visualization SQL queries return data."""
    query = "SELECT * FROM high_risk_areas LIMIT 1;"
    data = fetch_data(query)
    assert not data.empty
    assert "borough" in data.columns
