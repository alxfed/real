"""
Lots and the history of parcels, mergers and splits

data is from datacatalog cookcountyil gov
"""


# socrata access
SOCRATA_TOKEN_FILE = 'socrata_API_token.txt'

with open(SOCRATA_TOKEN_FILE, 'r') as token_file:   # open the file and read the token
    token = token_file.read().rstrip('\n')
    token_file.close()                              # clean up

# domain of the end-point for parcels and PLSS
CC_END_POINT_DOMAIN = 'datacatalog.cookcountyil.gov' # with leading https://

'''
Parcel 2000 Field Names:
the_geom, 
pin10, pin14, pina, pinsa, pinb, pinp, pinu, pinac,
taxcode, job_no, parceltype, upper_elev, lower_elev,
shape_area, shape_len
'''

CCGISDATA_PARCEL_2000 = 'bbcr-ryng' # map page /GIS-Maps/ccgisdata-Parcel-2000/x2ib-rt29
CCGISDATA_PARCEL_2001 = 't799-vjyq' # map page /GIS-Maps/ccgisdata-Parcel-2001/i2km-7cwi
CCGISDATA_PARCEL_2002 = 'dckf-92bv' # map page /GIS-Maps/ccgisdata-Parcel-2002/3wb8-2she
CCGISDATA_PARCEL_2003 = 'anwy-2bet' # map page /GIS-Maps/ccgisdata-Parcel-2003/gcqr-kbqq
CCGISDATA_PARCEL_2004 = 'sg9a-x6ka' # map page /GIS-Maps/ccgisdata-Parcel-2004/6jt3-ndyu
CCGISDATA_PARCEL_2005 = '7emi-v3x2' # map page /GIS-Maps/ccgisdata-Parcel-2005/f42p-dbfm


# The list of datasets
AVAILABLE_DATASETS = [CCGISDATA_PARCEL_2000, CCGISDATA_PARCEL_2001, CCGISDATA_PARCEL_2002,
                      CCGISDATA_PARCEL_2003, CCGISDATA_PARCEL_2004, CCGISDATA_PARCEL_2002]


from sodapy import Socrata
import pandas as pd

with Socrata(CC_END_POINT_DOMAIN, token) as client:
    chunk = client.get(CCGISDATA_PARCEL_2000, limit=2)    # Read a couple of lines
    client.close()

dta = pd.DataFrame.from_dict(chunk)
print(dta)

