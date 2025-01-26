# ETL Pipeline for NYC Motor Vehicle Collisions Data

## Project Description
The **ETL Pipeline for NYC Motor Vehicle Collisions Data** is a Python-based application designed to automate the extraction, transformation, and loading (ETL) process for traffic collision data from the NYC Open Data API. The pipeline processes data about motor vehicle collisions, injuries, fatalities, and vehicle types, storing the results in an SQL Server database for analysis and reporting.

This project is ideal for practicing real-world data engineering skills such as API integration, data transformation, database interaction, and workflow automation.

## Features
- **Data Source**: Extracts live collision data from the [NYC Open Data API](https://data.cityofnewyork.us/resource/h9gi-nx95.json).
- **Transformation**: Cleans, validates, and enriches the data.
- **Database Integration**: Loads the processed data into a SQL Server database.
- **Logging**: Tracks the ETL process in log files for monitoring and debugging.
- **Modular Design**: Divides the pipeline into reusable components for scalability.

## Prerequisites
Before running the project, ensure you have:
- **Python 3.8 or higher**
- **PostgreSQL installed and running** 
- **psql** command-line tool installed
- **Git** installed on your system
- Python libraries listed in `requirements.txt`

## Installation and Setup

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/udaybjoshi/etl_nyc_collision_data.git
cd etl_nyc_collision_dataß
```

### 2. Set Up the Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Configure Database
- Create a new database in PostgreSQL
```bash 
CREATE DATABASE nyc_collision;
```

- Update the .env file with the database credentials:
```bash
DB_NAME = nyc_collision
DB_USER = your_username
DB_PASSWORD = your_password
DB_HOST = localhost
DB_PORT = 5432
```

### 4. Run the ETL Pipeline
- Execute the main ETL script:
```bash
python scripts/etl_pipeline.py
```

### 5. Test the Pipeline
- Run unit tests:
```bash
python -m unittest discover tests
```

### 6. View Logs
- Check logs for pipeline execution in 'logs/etl_log.txt'

## Database Configuration
The database connection details are stored in the 'config/db_config.py' file. This script reads credentials from the '.env' file and establishes a connection to the PostgreSQL database.

Example db_config.py:
```bash
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
```
## Notes
- Make sure the PostgreSQL service is running before executing the ETL pipeline.
- If you encounter connection issues, verify the '.env' file and database settings.

