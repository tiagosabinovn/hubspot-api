import requests
import json
from decimal import Decimal
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, collect_list, concat_ws, max, sum, count, lit, concat, when, avg, isnull, desc, asc, collect_set

# Initialize the Spark Session
spark = SparkSession.builder.appName("HubSpotIntegration").getOrCreate()

# Execute the SQL query to obtain the data
query = """
-- Place the SQL query here

-- Thats a example query 
-- Select id, created_at, count(distinct user_id) as users, sum(value) as values from table.example group by 1, 2
"""

# Execute the query and obtain the DataFrame
schools_df = spark.sql(query)

# Fill null values with 0
schools_df = schools_df.fillna({
    "values": 0
})

# Convert dates to the yyyy-MM-dd format
date_columns = [
    "created_at"
]

for col_name in date_columns:
    schools_df = schools_df.withColumn(col_name, date_format(col(col_name), "yyyy-MM-dd"))

# HubSpot API details
HUBSPOT_API_KEY = "your-token-here"
HUBSPOT_API_URL = "https://api.hubapi.com/crm/v3/objects/companies/"

print("Import started successfully")

# Function to get a company in the HubSpot CRM by id
def get_company_by_id(id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HUBSPOT_API_KEY}"
    }
    data = {
        "filters": [
            {
                "propertyName": "id",
                "operator": "EQ",
                "value": id
            }
        ],
        "limit": 1,
        "properties": ["id"]
    }
    
    response = requests.post(HUBSPOT_API_URL + "search", headers=headers, data=json.dumps(data))
    response.raise_for_status()
    results = response.json().get('results', [])
    if results:
        return results[0]
    return None

# Function to update the company properties in the HubSpot CRM
def update_company_properties(company_id, properties):
    url = f"{HUBSPOT_API_URL}{company_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HUBSPOT_API_KEY}"
    }
    
    serializable_properties = {}
    for key, value in properties.items():
        if value is None:
            value = None
        elif isinstance(value, Decimal):
            serializable_properties[key] = float(value)
        elif isinstance(value, (int, float)):
            serializable_properties[key] = value
        elif isinstance(value, str):
            serializable_properties[key] = value
            
    data = {
        "properties": serializable_properties
    }
    
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()

# Process each row of the DataFrame and update the company properties in HubSpot
for row in schools_df.collect():
    id = row['id']
    company = get_company_by_id(id)
    
    if company:
        company_id = company['id']
        properties = row.asDict()
        properties = {k: v for k, v in properties.items() if v is not None}
        
        try:
            update_company_properties(company_id, properties)
        except requests.exceptions.HTTPError as e:
            print(f"Failed to import company with {company_id} and id {id}")
            print(f"Error: {e}")
            print(f"Data sent: {properties}")
        except Exception as e:
            print(f"Unexpected error updating company with {company_id} and id {id}")
            print(f"Error: {e}")
    else:
        print(f"No company found with id {id}")

print("Process completed.")

