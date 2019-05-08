"""
Last available full set of parcels (2016)
"""


import json
import requests
import pandas as pd

RESOURCE_URL = 'datacatalog.cookcountyil.gov'
PARCELS_2016 = '6gsb-287d'                      # Last available full Parcels shapes set
TOKEN_FILE   = 'socrata_API_token.txt'

with open(TOKEN_FILE, 'r') as api_token_file:       # zoning app token
    api_token = api_token_file.read().rstrip('\n')
    api_token_file.close()

api_url = f'https://{RESOURCE_URL}/resource/{PARCELS_2016}.json'

header = {'Content-Type': 'application/json',
           'X-App-Token': api_token}


# ?$$exclude_system_fields=false
# adds
# :id	The internal Socrata identifier for this record.
# :created_at	A Fixed Timestamp representing when this record was created.
# :updated_at	A Fixed Timestamp representing when this record was last updated.
# then you can use $select=:id  in your requests


def data_chunk(uri):
    response = requests.get(uri, headers=header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    elif response.status_code == 201:
        raise RuntimeError("Request Processing")
    elif response.status_code == 400:
        raise RuntimeError("Bad Request")
    elif response.status_code == 401:
        raise RuntimeError("Unauthorized")
    elif response.status_code == 403:
        raise RuntimeError("Forbidden")
    elif response.status_code == 404:
        raise RuntimeError("Not Found")
    elif response.status_code == 429:
        raise RuntimeError("Too many Requests")
    elif response.status_code == 500:
        raise RuntimeError("Server Error")
    else:
        return None # silently return nothing

#line_id = ':id == alkjdflkajsdlfkj'
#api_call = api_url + f'?where={line_id}'


'''	
# Read a chunk with sale_date in predefined window	

start_year = 2018
start_dt = dt.datetime(year=start_year,
                    month=12, day=1, hour=0,
                    minute=0, second=0)
start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S')

end_year = 2018
end_dt = dt.datetime(year=end_year,
                  month=12, day=2, hour=0,    # the first empty day in the dataset (End of it)
                  minute=0, second=0)
end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S')


api_call = api_url + f'?$where=sale_date between {start_str!r} and {end_str!r}'
'''
limit = 1000    # limit of a frame within the time window
offset = 0      # offset of the frame within the time window
api_frame = api_url + f'?$limit={limit}&$offset={offset}'

#https://datacatalog.cookcountyil.gov/resource/6gsb-287d.json
dst = data_chunk(api_frame)

if dst:
    print("Here's your info: ")
    new_chunk = pd.DataFrame.from_records(dst)

else:
    print('[!] Request Failed')


print('ok!')