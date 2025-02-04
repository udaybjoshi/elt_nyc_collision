# ELT Pipeline for NYC Motor Vehicle Collisions Data

## Project Description
The **ELT Pipeline for NYC Motor Vehicle Collisions Data** is a Python-based application designed to automate the extraction, transformation, and loading (ETL) process for traffic collision data from the NYC Open Data API. The pipeline processes data about motor vehicle collisions, injuries, fatalities, and vehicle types, storing the results in an MySQL database for analysis and reporting.

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

## 📂 Project Folder Structure
elt_nyc_collision/
│── config/                      # Configuration files (e.g., environment variables, database settings)
│   ├── db_config.py               # Database connection details
│   ├── logging_config.py          # Logging settings
│
│── data/                         # Data storage folder
│   ├── input/                     # Raw input data (CSV, JSON, etc.)
│   │   ├── raw_api_data.csv       # Raw collision data from external API
│   │
│   ├── output/                   # Processed/cleaned data ready for analysis
│   │   ├── cleaned_api_data.csv   # Preprocessed collision data
│   │   ├── transformed_data.csv   # Transformed data ready for MySQL insertion
│
│── logs/                         # Logs for ELT pipeline runs
│   ├── source_pipeline.log        # Logs for raw data extraction
│   ├── staging_pipeline.log       # Logs for data transformation & staging
│   ├── entities_pipeline.log      # Logs for final data transfer
│
│── scripts/                      # ELT scripts and analysis functions
│   ├── extract.py                  # Extract raw data from API
│   ├── load_source.py              # Load raw data into MySQL source table
│   ├── load_staging.py             # Process and move data from source to staging table
│   ├── load_entities.py            # Load validated data into the final entities table
│   ├── transform.py                # Data transformation logic
│   ├── analysis.py                 # Visualizations and analytics on processed data
│   ├── create_views.sql            # SQL scripts to create database views
│
│── tests/                        # Unit tests for pipeline validation
│   ├── test_etl.py                # Tests for raw data extraction
│
│── requirements.txt               # Python dependencies
│── .gitignore                     # Ignore unnecessary files (e.g., .env, logs, data files)
│── README.md                      # Project documentation


## Features
- **Data Source**: Extracts live collision data from the [NYC Open Data API](https://data.cityofnewyork.us/resource/h9gi-nx95.json).
- **Transformation**: Cleans, validates, and enriches the data.
- **Database Integration**: Loads the processed data into a MySQL database.
- **Logging**: Tracks the ELT process in log files for monitoring and debugging.
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
git clone https://github.com/udaybjoshi/elt_nyc_collision.git
cd elt_nyc_collision
```

### 3. Set Up the Virtual Environment and Install Dependencies
```bash
python -m venv .venv
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

### 5. Test the ELT Pipeline
- Run unit tests:
```bash
python -m pytest tests/test_etl.py --disable-warnings
```

### 6. Run the ELT Pipeline
- Execute the different steps of the ETL process:
```bash
python scripts/load_source.py    # Extract raw data
python scripts/load_staging.py   # Transforma and load into staging table
python scripts/load_entities.py  # Load into final entities tables   
```

### 7. Run Data Analysis
- Create visualizations based on consumption layer views:
```bash
python scripts/analysis.py
```

### 8. View Logs
- Check logs for pipeline execution 
```bash
cat logs/source_pipeline.log
cat logs/staging_pipeline.log
cat logs/entities_pipeline.log
```

## Database Configuration
The database connection details are stored in the `config/db_config.py` file. This script reads credentials from the `.env` file and establishes a connection to the MySQL database.

## Notes
- Make sure the MySQL service is running before executing the ETL pipeline.
- If you encounter connection issues, verify the `.env` file and database settings.

## Licence
This project is licensed under the MIT License - see the LICENSE file for details.



