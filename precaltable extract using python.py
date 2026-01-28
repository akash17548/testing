import requests
import pandas as pd

# API details
base_url = "base_url"
base_path = "endpoint"
username = "username"
password = "password"

# Input parameters


#Build payload
payload = {
    "endRow": 300,
    "operationType": "fetch",
    "startRow": 0,
    "textMatchStyle": "exact",
    "data": {
        "criteria":  [{'fieldName': 'Material', 'operator': 'iContains', 'value': '500005893'},
                       {'fieldName': 'PricingDate', 'operator': 'greaterOrEqual', 'value': '2024-09-26'},
                         {'fieldName': 'PricingDate', 'operator': 'lessOrEqual', 'value': '2024-09-26'},
                           {'fieldName': 'Hierarchy', 'operator': 'iContains', 'value': '0011528597'}
                           ]

    }
}
    
# # Make POST request with basic auth
response = requests.post(
    base_url + base_path,
    json=payload,                     # send JSON body
    auth=(username, password),        # basic authentication
   
)
# Parse JSON
resp_json = response.json()
    
# Extract "data" array
data = resp_json.get("response", {}).get("data", [])
total_rows = resp_json.get("response", {}).get("totalRows", 0)
print(f"\nTotal Rows: {total_rows}")
# # Clean null values from each row
cleaned = []
for row in data:
      non_null_row = {k: v for k, v in row.items() if v is not None and "L" in k}
      List = cleaned.append(non_null_row)
print("\nCleaned Data:")
print(cleaned)
# # # Convert to DataFrame
df = pd.DataFrame(cleaned)
print("\nDataFrame:")
print(df)

# #Choose the columns you want weighted averages for
columns_to_average = ["ZP01L","ZT43L","ZT24L","ZPV0L"]

# # Dictionary to store results
weighted_avgs = {}

# # Loop through each column
if total_rows > 0:
     for col in columns_to_average:
      weighted_avg = (df[col] * df["TVOL"]).sum() / df["TVOL"].sum()
      weighted_avgs[col] = float(weighted_avg)

else:
      print(df)    

print(weighted_avgs)