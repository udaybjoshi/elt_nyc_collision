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
- **Python 3.6 or higher**
- **SQL Server and SSMS** (SQL Server Management Studio)
- **Git** installed on your system
- Python libraries listed in `requirements.txt`

## Installation and Setup

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/udaybjoshi/etl_nyc_collision_data.git
cd etl_nyc_collision_dataß
