"""
Working with socrata where some of the data is
"""


from sodapy import Socrata
import pandas as pd

with open('socrata_API_token.txt', 'r') as token_file: # zoning and permits app
    token = token_file.read().rstrip('\n')
    token_file.close()

with Socrata("data.cityofchicago.org", token) as client:
    # the dataset Id on the page (for copying) is 'building-permits'
    # and it works with client.get, however, it doesn't work with
    # .get_metadata.
    # the other Id for the same is ydr8-5enu (checked the resulting data
    # https://dev.socrata.com/foundry/data.cityofchicago.org/ydr8-5enu
    # with it the client.get_metadata gives the right response.
    meta_of_set = client.get_metadata('ydr8-5enu')     # Building permits
    column_names = [x['name'] for x in meta_of_set['columns']]
    re = client.get('ydr8-5enu', limit=2)
    client.close()

sm = pd.DataFrame.from_dict(re)

print(sm)

# Assessment data in socrata https://datacatalog.cookcountyil.gov/resource/bcnq-qi2z.json

with Socrata("datacatalog.cookcountyil.gov", token) as client:
    re = client.get("bcnq-qi2z", limit=2) # final assessment
    da = client.get('5pge-nu6u', limit=2) # assessment data
    lt = client.get('urmr-mchf', limit=2) # LOT - 2016 lots map from Assessor
    client.close()

sm = pd.DataFrame.from_dict(re)
dta = pd.DataFrame.from_dict(da)

print(dta)

# Zoning districts data https://data.cityofchicago.org/resource/dj47-wfun.json