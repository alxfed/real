"""
Socrata discovery API
"""


import json
import datetime as dt
import requests

COOKCOUNTY_DOMAIN = 'datacatalog.cookcountyil.gov'
CITYOFCHICAGO_DOMAIN = 'data.cityofchicago.org'

SOCRATA_CATALOG_URL = 'api.us.socrata.com/api/catalog/v1'

def answer(uri):
    response = requests.get(uri)
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



facets_uri = f'https://{SOCRATA_CATALOG_URL}/domains/{CITYOFCHICAGO_DOMAIN}/facets'

facet_response = answer(facets_uri)

for one in facet_response:
    print(one['facet'], '\t', one['count'])


# facets of a domain
# http://api.us.socrata.com/api/catalog/v1/domains/domain/facets

# in particular
# http://api.us.socrata.com/api/catalog/v1/domains/datacatalog.cookcountyil.gov/facets

# and
# http://api.us.socrata.com/api/catalog/v1/domains/data.cityofchicago.org/facets

# then count by categories in the domain (facets)
# http://api.us.socrata.com/api/catalog/v1/domain_categories=

# http://api.us.socrata.com/api/catalog/v1?domains=datacatalog.cookcountyil.gov&search_context=datacatalog.cookcountyil.gov&limit=600

# http://api.us.socrata.com/api/catalog/v1?categories=Education&tags=families&search_context=data.seattle.gov

