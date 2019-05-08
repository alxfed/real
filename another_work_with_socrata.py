"""
Assessor Data processing
"""


import json
import datetime as dt
import requests
import pandas as pd

RESOURCE_URL = 'datacatalog.cookcountyil.gov'
RESOURCE_ID  = '5pge-nu6u'                      # Modelling data
TOKEN_FILE   = 'socrata_API_token.txt'

with open(TOKEN_FILE, 'r') as api_token_file:       # zoning app token
    api_token = api_token_file.read().rstrip('\n')
    api_token_file.close()

api_url = f'https://{RESOURCE_URL}/resource/{RESOURCE_ID}.json'

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
# Read a predefined chunk with predefined offset	
lim = 1000	
offs = 0	
api_call = api_url + f'?$limit={lim}&$offset={offs}'	
'''

'''	
# Read a chunk with sale_date in predefined window	
'''
start_year = 2018
start_dt = dt.datetime(year=start_year,
                    month=11, day=30, hour=0,
                    minute=0, second=0)
start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S')

end_year = 2018
end_dt = dt.datetime(year=end_year,
                  month=12, day=1, hour=0,
                  minute=0, second=0)
end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S')
limit = 1000    # limit of a frame within the time window
offset = 2      # offset of the frame within the time window

api_call = api_url + f'?$where=sale_date between {start_str!r} and {end_str!r}'
api_frame = api_call + f'&$limit={limit}&$offset={offset}'

dst = data_chunk(api_frame)

if dst is not None:
    print("Here's your info: ")
    new_chunk = pd.DataFrame.from_records(dst)
    new_chunk['sale_date'] = pd.to_datetime(new_chunk['sale_date'])

else:
    print('[!] Request Failed')


print('ok!')

# info['sale_date'] = str(info['sale_date']) - Nope of course

# long complex request

api_url = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and '2015-01-10T14:00:00'"

# date-time or "floating timestamp" are in ISO8601 Times
# https://en.wikipedia.org/wiki/ISO_8601#Times

dst = rqst() # works

# url string formation

api_url_base = 'data.cityofchicago.org'
api_resource_id = 'ydr8-5enu'

api_url = 'https://{}/resource/{}.json'.format(api_url_base, api_resource_id)

# but f-string for complex requests _for sure_

requ = 'where'
argu = ''

api_request = f'{api_url}?${requ}={argu}'

# but if the parameters of the query are already in a dictionary
# then the trick is:


person = {'name': 'Alex', 'age': 64}
message = "Hello, {name}. You are {age}.".format(**person)
