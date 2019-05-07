import json
import requests
import pandas as pd

with open('socrata_API_token.txt', 'r') as token_file: # zoning and permits app
    api_token = token_file.read().rstrip('\n')
    token_file.close()

api_url = 'https://datacatalog.cookcountyil.gov/resource/5pge-nu6u.json'
headers = {'Content-Type': 'application/json',
           'X-App-Token': api_token}
def rqst():
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

dst = rqst()

if dst is not None:
    print("Here's your info: ")
    pass

else:
    print('[!] Request Failed')

info = pd.DataFrame.from_records(dst)  # it would work for dictionaries too
info['sale_date'] = pd.to_datetime(info['sale_date'])



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
