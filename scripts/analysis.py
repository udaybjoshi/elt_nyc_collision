import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection details from .env file
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "nyc_collision"
DB_USER = "root"
DB_PASSWORD = "p!55word"

# Verify DB connection
print(f"Connecting to MySQL server at {DB_HOST}:{DB_PORT} with user {DB_USER}")

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Ensure output directory exists
output_dir = "/Users/mac/Documents/MentorCruise/Projects/etl_nyc_collision/data/output"
os.makedirs(output_dir, exist_ok=True)

def fetch_data(query):
    """
    Fetch data from the database using a SQL query.

    Parameters:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
    try:
        with engine.connect() as connection:
            return pd.read_sql(query, connection)
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise

# 1. High-Risk Areas Visualization
def visualize_high_risk_areas():
    """
    Visualize the top 10 high-risk areas for collisions by borough.

    Insight:
        This visualization highlights streets with the highest collision counts,
        enabling targeted safety measures like adding traffic lights or reducing speed limits.
    """
    query = "SELECT borough, SUM(total_collisions) AS total_collisions FROM high_risk_areas GROUP BY borough;"
    
    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for collisions by borough.")
            return
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x="borough", y="total_collisions", data=data, palette="viridis")
        plt.title("Total Collisions by Borough")
        plt.xlabel("Borough")
        plt.ylabel("Total Collisions")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/collisions_by_borough.png")
        plt.close()

        print(f"Visualization saved: {output_dir}/collisions_by_borough.png")
    except Exception as e:
        print(f"Error visualizing collisions by borough: {e}")
        raise

# 2. Collision Severity Trends
def visualize_collision_severity_trends():
    """
    Visualize the trends in injuries and fatalities over time.

    Insight:
        Observing an upward trend in fatalities may indicate a need for immediate intervention,
        while a downward trend could highlight the effectiveness of safety campaigns.
    """
    query = "SELECT collision_date, total_injuries, total_fatalities FROM collision_severity_trends;"

    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for collision severity trends.")
            return
        
    
        plt.figure(figsize=(14, 7))
        sns.lineplot(x="collision_date", y="total_injuries", label="Injuries", data=data)
        sns.lineplot(x="collision_date", y="total_fatalities", label="Fatalities", data=data, color="red")
        plt.title("Collision Severity Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.legend(title="Severity")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/collision_severity_trends.png")
        plt.close()

        print(f"Visualization saved: {output_dir}/collision_severity_trends.png")
    except Exception as e:
        print(f"Error visualizing collision severity trends: {e}")
        raise

# 3. Contributing Factors Analysis
def visualize_contributing_factors():
    """
    Visualize the top contributing factors to collisions.

    Insight:
        Identifying common factors like speeding or distracted driving allows for
        targeted public awareness campaigns and law enforcement actions.
    """
    query = "SELECT contributing_factor, total_collisions FROM contributing_factors_analysis LIMIT 10;"

    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for contributing factors analysis.")
            return

        plt.figure(figsize=(12, 6))
        sns.barplot(x="total_collisions", y="contributing_factor", data=data)
        plt.title("Top Contributing Factors to Collisions")
        plt.xlabel("Total Collisions")
        plt.ylabel("Contributing Factor")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/contributing_factors.png")
        plt.close()

        print(f"Visualization saved: {output_dir}/contributing_factors.png")
    except Exception as e:
        print(f"Error visualizing contributing factors: {e}")
        raise

# 4. Cyclist and Pedestrian Safety Concerns
def visualize_cyclist_pedestrian_safety():
    """
    Visualize pedestrian and cyclist injuries and fatalities by borough.

    Insight:
        Boroughs with high pedestrian or cyclist incidents can prioritize the development
        of bike lanes, crosswalks, and traffic calming measures.
    """
    query = """
        SELECT borough, pedestrians_injured, pedestrians_killed, cyclists_injured, cyclists_killed
        FROM cyclist_pedestrian_safety;
    """
    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for cyclist pedestrian safety.")
            return

        data = data.melt(id_vars=["borough"], var_name="Metric", value_name="Count")
        plt.figure(figsize=(14, 7))
        sns.barplot(x="borough", y="Count", hue="Metric", data=data)
        plt.title("Cyclist and Pedestrian Safety Concerns by Borough")
        plt.xlabel("Borough")
        plt.ylabel("Count")
        plt.legend(title="Metric", loc="upper right")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/cyclist_pedestrian_safety.png")
        plt.close()

        print(f"Visualization saved: {output_dir}/cyclist pedestrian safety.png")
    except Exception as e:
        print(f"Error cyclist pedestrian safety: {e}")
        raise

# 5. Time-Based Collision Patterns
def visualize_time_based_patterns():
    """
    Visualize the distribution of collisions by hour of the day.

    Insight:
        High collision counts during specific hours (e.g., rush hours) can guide
        adjustments in traffic flow management or law enforcement deployment.
    """
    query = "SELECT hour_of_day, total_collisions FROM time_based_collision_patterns;"

    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for time based collision patterns.")
            return

        plt.figure(figsize=(12, 6))
        sns.barplot(x="hour_of_day", y="total_collisions", data=data, palette="coolwarm")
        plt.title("Collisions by Hour of Day")
        plt.xlabel("Hour of Day")
        plt.ylabel("Total Collisions")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/time_based_patterns.png")
        plt.close()

        print(f"Visualization saved: {output_dir}/time based collision patterns.png")
    except Exception as e:
        print(f"Error time based collision patterns: {e}")
        raise

# 6. Monthly Trends
def visualize_monthly_dashboard():
    """
    Visualize monthly trends in collisions, injuries, and fatalities.

    Insight:
        This dashboard helps identify seasonal trends or months with unusually high incident rates.
    """
    query = """
        SELECT 
            YEAR(crash_date) AS year, 
            MONTH(crash_date) AS month, 
            COUNT(*) AS total_collisions, 
            SUM(number_of_persons_injured) AS total_injuries, 
            SUM(number_of_persons_killed) AS total_fatalities
        FROM collision_data
        GROUP BY YEAR(crash_date), MONTH(crash_date)
        ORDER BY year, month;
    """
    
    try:
        data = fetch_data(query)
        if data.empty:
            print("No data available for monthly trends.")
            return
        
        # Create a datetime column for plotting
        data["month_year"] = pd.to_datetime(data["year"].astype(str) + "-" + data["month"].astype(str))

        plt.figure(figsize=(14, 7))
        sns.lineplot(x="month_year", y="total_collisions", label="Collisions", data=data)
        sns.lineplot(x="month_year", y="total_injuries", label="Injuries", data=data, color="green")
        sns.lineplot(x="month_year", y="total_fatalities", label="Fatalities", data=data, color="red")
        plt.title("Monthly Collision Trends")
        plt.xlabel("Month")
        plt.ylabel("Count")
        plt.legend(title="Metric")
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        print(f"Visualization saved: {output_dir}/monthly trends.png")
    except Exception as e:
        print(f"Error monthly trends: {e}")
        raise
    
    except Exception as e:
        print(f"Error visualizing monthly collision trends: {e}")
        raise



if __name__ == "__main__":
    try:
        visualize_high_risk_areas()
        visualize_collision_severity_trends()
        visualize_contributing_factors()
        visualize_cyclist_pedestrian_safety()
        visualize_time_based_patterns()
        visualize_monthly_dashboard()
        # Add calls to other visualization functions here
    except Exception as e:
        print(f"Error in main execution: {e}")

