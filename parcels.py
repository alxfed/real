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
CCGISDATA_PARCEL_2006 = 'w98x-3iwy' # map page /GIS-Maps/ccgisdata-Parcel-2006/r5e4-5wi6
CCGISDATA_PARCEL_2007 = 'spy4-y5mz' # map page /GIS-Maps/ccgisdata-Parcel-2007/mvxv-d4di
CCGISDATA_PARCEL_2008 = 'ueaz-2czr' # map page /GIS-Maps/ccgisdata-Parcel-2008/54r5-cenp
CCGISDATA_PARCEL_2009 = 'abae-6ajx' # map page /GIS-Maps/ccgisdata-Parcel-2009/5rc6-e9r6
CCGISDATA_PARCEL_2010 = 'nhsi-bt2g' # map page /GIS-Maps/ccgisdata-Parcel-2010/fgrb-v8fq
CCGISDATA_PARCEL_2011 = '673u-r3as' # map page /GIS-Maps/ccgisdata-Parcel-2011/9u3u-ac9c
CCGISDATA_PARCEL_2012 = '3j29-aw9a' # map page /GIS-Maps/ccgisdata-Parcel-2012/e62c-6rz8
CCGISDATA_PARCEL_2013 = '3git-3hp2' # map page /GIS-Maps/ccgisdata-Parcel-2013/5i2c-y2u6
CCGISDATA_PARCEL_2014 = 'yf2z-xf2p' # map page /GIS-Maps/ccgisdata-Parcel-2014/2m9h-cq6j
'''
Parcel 2015 field names:
the_geom
pin10, pin14, pinsa, pinb, pinp, pinu, pinac
taxcode, job_no, parceltype, upper_elev, lower_elev
survey_cal, shape_star, shape_stle
'''
CCGISDATA_PARCEL_2015 = 'trnc-t2et' # map page /GIS-Maps/ccgisdata-Parcel-2015/nxb6-rw3s

'''
Parcels 2016 field names:
objectid, name, 
the_geom, 
pin10, <no pin14>, pina, pinsa, pinb, pinp, pinu, pinac,
taxcode, job_no, parceltype, upper_elev, lower_elev,
survey_cal, shape_star, shape_stle
'''
CCGISDATA_PARCELS_2016= '6gsb-287d' # map page /GIS-Maps/ccgisdata-Parcels-2016/a33b-b59u


# The list of datasets
AVAILABLE_DATASETS = [CCGISDATA_PARCEL_2000, CCGISDATA_PARCEL_2001, CCGISDATA_PARCEL_2002,
                      CCGISDATA_PARCEL_2003, CCGISDATA_PARCEL_2004, CCGISDATA_PARCEL_2005,
                      CCGISDATA_PARCEL_2006, CCGISDATA_PARCEL_2007, CCGISDATA_PARCEL_2008,
                      CCGISDATA_PARCEL_2009, CCGISDATA_PARCEL_2010, CCGISDATA_PARCEL_2011,
                      CCGISDATA_PARCEL_2012, CCGISDATA_PARCEL_2013, CCGISDATA_PARCEL_2014,
                      CCGISDATA_PARCEL_2015, CCGISDATA_PARCELS_2016]


from sodapy import Socrata
import pandas as pd

with Socrata(CC_END_POINT_DOMAIN, token) as client:
    chunk = client.get(CCGISDATA_PARCELS_2016, limit=2)    # Read a couple of lines
    client.close()

dta = pd.DataFrame.from_dict(chunk)
print(dta)

