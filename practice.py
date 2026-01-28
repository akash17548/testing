import pandas as pd
response_json={
    "response": {
        "status": 0,
        "startRow": 0,
        "data": [
            {
                "Material": "500005893",
                "Hierarchy": "0011528597"
            },{
                "Material": "50000578",
                "Hierarchy": "0011528567"
            }
            ]
            }
            }
total_rows =2
List =[]
dictionary={}
value=response_json.get("response",{})

print(value)