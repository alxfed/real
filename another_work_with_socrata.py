import json
import requests

with open('socrata_API_token.txt', 'r') as token_file: # zoning and permits app
    api_token = token_file.read().rstrip('\n')
    token_file.close()

api_url = 'https://data.cityofchicago.org/resource/ydr8-5enu.json'
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

print('ok!')

# url string formation

api_url_base = 'https://data.cityofchicago.org/resource/'
api_resource_id = 'ydr8-5enu.json'

api_url = '{}orgs/{}/repos'.format(api_url_base, api_resource_id)

# but f-string for complex requests _for sure_

requ = 'where'
loc = ''

api_request = f'{api_url}?${requ}={loc}'

# but if the parameters of the query are in a dictionary
# then the trick is:

'''
person = {'name': 'Alex', 'age': 64}
"Hello, {name}. You are {age}.".format(**person)
'''