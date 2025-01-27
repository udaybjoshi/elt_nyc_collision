import pandas as pd
from dotenv import load_dotenv
import os
import mysql.connector

csv_file_path = "./data/input/raw_api_data.csv"  # Path to the CSV file

data = pd.read_csv(csv_file_path)
print(data.info())  # Check the structure of the DataFrame
print(data.isnull().sum())  # Ensure no NaN values remain

data = data.where(pd.notnull(data), None)
print(data.isnull().sum())  # Ensure no NaN values remain


