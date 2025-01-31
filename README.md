# ETL Pipeline for NYC Motor Vehicle Collisions Data

## Project Description
The **ETL Pipeline for NYC Motor Vehicle Collisions Data** is a Python-based application designed to automate the extraction, transformation, and loading (ETL) process for traffic collision data from the NYC Open Data API. The pipeline processes data about motor vehicle collisions, injuries, fatalities, and vehicle types, storing the results in an MySQL database for analysis and reporting.

## Business Context
The NYC Collision Data project aims to analyze vehicle collisions in New York City to **improve public safety, optimize city planning, and support research efforts** by leveraging insights from historical collision data. The data includes information on crash dates, times, locations, contributing factors, and the severity of incidents.

## Business Goals
### 1. Public Safety:
- Identify high-risk areas (collision hotspots) to focus safety measures.
- Analyze trends in the severity of collisions (injuries and fatalities).
- Determine common contributing factors to collisions to inform public awareness campaigns.
### 2. City Planning:
- Use location-based collision data to recommend infrastructure improvements (e.g., road repairs, traffic lights).
- Understand pedestrian and cyclist safety concerns to guide the allocation of bike lanes and crosswalks.
### 3. Policy and Law Enforcement:
- Identify patterns related to time of day, weather conditions, and other factors that lead to accidents.
- Evaluate the effectiveness of existing traffic laws and propose necessary adjustments.
### 4. Research and Reporting:
- Create public-facing dashboards and periodic reports for stakeholders (e.g., city officials, law enforcement, and researchers).
- Share insights with insurance companies, urban developers, and NGOs.

## Features
- **Data Source**: Extracts live collision data from the [NYC Open Data API](https://data.cityofnewyork.us/resource/h9gi-nx95.json).
- **Transformation**: Cleans, validates, and enriches the data.
- **Database Integration**: Loads the processed data into a MySQL database.
- **Logging**: Tracks the ETL process in log files for monitoring and debugging.
- **Modular Design**: Divides the pipeline into reusable components for scalability.

## Prerequisites
Before running the project, ensure you have:
- **Python 3.8 or higher**
- **MySQL Server** (8.0+ recommended) 
- **Git** installed on your system
- Python libraries listed in `requirements.txt`

## Installation and Setup

### 1. Install MySQL
- Download MySQL: [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/)
- Follow the installation instructions for your operating system.
- Configure MySQL with a user and password for this project.

### 2. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/udaybjoshi/etl_nyc_collision.git
cd etl_nyc_collision
```

### 3. Set Up the Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure Database
- Log in to MySQL:
```bash
mysql -u root -p
```
- Create a new database in MySQL
```bash 
CREATE DATABASE nyc_collision;
```
- Switch to the `nyc_collision` database:
```bash
USE nyc_collision
```

- Update the .env file with the database credentials:
```bash
DB_NAME = nyc_collision
DB_USER = root
DB_PASSWORD = your_password
DB_HOST = localhost
DB_PORT = 3306
```

### 5. Run the ETL Pipeline
- Execute the main ETL script:
```bash
python scripts/etl_pipeline.py
```

### 6. Test the Pipeline
- Run unit tests:
```bash
python -m pytest tests/test_etl.py --disable-warnings
```

### 7. View Logs
- Check logs for pipeline execution in `logs/etl_log.txt`

## Database Configuration
The database connection details are stored in the `config/db_config.py` file. This script reads credentials from the `.env` file and establishes a connection to the MySQL database.

## Notes
- Make sure the MySQL service is running before executing the ETL pipeline.
- If you encounter connection issues, verify the `.env` file and database settings.

## Licence
This project is licensed under the MIT License - see the LICENSE file for details.



