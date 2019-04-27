"""
Cadaster system in Chicago as of 2014
"""

'''
Survery Township
The Public Land Survey System (PLSS) forms the foundation of 
Cook County's cadastral system for identifying and locating 
land records. Tax parcels are identified using township and 
section notation, in a modified format. This PLSS feature data 
set is intended to correspond to tax pages in the Cook County 
Assessor's Tax Map book (current as of tax year 2000 for 66% 
of the County and as of tax year 2001 for the remaining 33% 
of the County), and should not be used for measurement or 
surveyor purposes. In addition, the parcel attributes PINA 
(area/township) and PINSA (subarea/section) do not necessarily 
correspond to the PLSS township and section polygon in which 
a given parcel resides. The PLSS data is modeled as a single 
composite network coverage that encompasses townships (area), 
sections (subarea), quarter sections, and half quarter section.
'''

# Survey Township   https://datacatalog.cookcountyil.gov/resource/iz5k-qtpu.json

'''
PLSS Line
The County's system of tax maps is based on the Illinois
Public Land Survey System (PLSS). In the PLSS, each township
is divided into 36 sections, and each section into four
quarter-sections. A quarter-section is further divided into
two tax map sheets, often called "pages". Each tax map
(1/4 mile by 1/2 mile) represents the east or west half of
one quarter-section, and typically there are eight tax maps
per section.
'''

# PLSS Line         https://datacatalog.cookcountyil.gov/resource/yvw8-g53g.json

'''
The PLSS data is modeled as a single composite network 
coverage that encompasses townships (area), sections (subarea), 
quarter sections, and half quarter section. If an indigenous 
people's reserve was present on the tax map, it was digitized 
to create subpolygons of the half-quarter section, and those 
polygons were attributed with the name of the reserve. Within 
this PLSS data set, a half-quarter section is the smallest 
polygon unit, except in cases where an Indigenous People's 
Reserve line is present.
'''

# Section           https://datacatalog.cookcountyil.gov/resource/xhzu-6w77.json