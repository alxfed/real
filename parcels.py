"""
Lots and the history of parcels, mergers and splits

data is from datacatalog cookcountyil gov
"""


# socrata access
SOCRATA_TOKEN_FILE = 'socrata_API_token.txt'

with open(SOCRATA_TOKEN_FILE, 'r') as token_file:   # open the file and read the token
    token = token_file.read().rstrip('\n')
    token_file.close()                              # clean up

# domain of the end-point

DOMAIN = 'datacatalog.cookcountyil.gov' # with leading https://

'''
Parcel 2000 Field Names:
the_geom, the_geom, PIN10, pin10,
PIN14, pin14, PINA, pina,
PINSA, pinsa, PINB, pinb,
PINP, pinp, PINU, pinu,
PINAC, pinac, TAXCODE, taxcode,
JOB_NO, job_no, PARCELTYPE, parceltype, 
UPPER_ELEV, upper_elev, LOWER_ELEV, lower_elev,
SHAPE_area, shape_area, SHAPE_len, shape_len
'''

CCGISDATA_PARCEL_2000 = 'bbcr-ryng' # map /GIS-Maps/ccgisdata-Parcel-2000/x2ib-rt29

