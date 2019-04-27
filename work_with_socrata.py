"""
Working with socrata where some of the data is
"""


from sodapy import Socrata
import pandas as pd

with open('socrata_API_token.txt', 'r') as token_file: # zoning and permits app
    token = token_file.read().rstrip('\n')
    token_file.close()

with Socrata("data.cityofchicago.org", token) as client:
    re = client.get("building-permits", limit=2)
    client.close()

sm = pd.DataFrame(re)

print(sm)

# Assessment data in socrata https://datacatalog.cookcountyil.gov/resource/bcnq-qi2z.json

with Socrata("datacatalog.cookcountyil.gov", token) as client:
    re = client.get("bcnq-qi2z", limit=2)
    client.close()

sm = pd.DataFrame(re)

print(sm)

# Zoning districts data https://data.cityofchicago.org/resource/dj47-wfun.json