import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
import sys

# Check and load environment variables
REQUIRED_ENV_VARS = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]

for var in REQUIRED_ENV_VARS:
    if os.getenv(var) is None:
        print(f"Error: Environment variable '{var}' is not set.")
        sys.exit(1)

# Set the Economist style
sns.set_theme(style="whitegrid", palette="pastel")
sns.set_context("talk")

# Database connection
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def fetch_data(query):
    """
    Fetch data from the database using a SQL query.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

# Visualization functions as provided
def visualize_high_risk_areas():
    """
    Visualize the top 10 high-risk areas for collisions by borough.

    Insight:
        This visualization highlights streets with the highest collision counts,
        enabling targeted safety measures like adding traffic lights or reducing speed limits.
    """
    query = "SELECT borough, on_street_name, total_collisions FROM high_risk_areas LIMIT 10;"
    data = fetch_data(query)
    plt.figure(figsize=(12, 6))
    sns.barplot(x="total_collisions", y="on_street_name", hue="borough", data=data)
    plt.title("Top 10 High-Risk Areas by Collisions")
    plt.xlabel("Total Collisions")
    plt.ylabel("Street Name")
    plt.legend(title="Borough", loc="upper right")
    plt.tight_layout()
    plt.savefig("output/high_risk_areas.png")
    plt.show()

# Repeat this function pattern for other visualizations...

if __name__ == "__main__":
    visualize_high_risk_areas()
    # Add other visualizations as required
