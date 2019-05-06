"""
Derived from the official Automated Appraisal codebase published by
CCAO (http://www.cookcountyassessor.com/) in 2019
Code: https://gitlab.com/ccao-data-science---modeling
Story: https://datacatalog.cookcountyil.gov/stories/s/p2kt-hk36
"""

'''
Modelling Data 
contains every valid arm’s length transaction in a specified geographic 
area and time period.  We define valid "arm’s length"
as a sale where the buyer and seller act independently and do not have 
any relationship to each other. We have included property characteristics 
at the time of sale, as well as location and property attributes for 
contextualization. Property characteristics include the number of rooms, 
bathrooms, size of garage, exterior construction of the property, and 
whether the home has a finished basement. Property Attributes include 
census tract, assessor neighborhood code, a geographically determined 
location factor, and street address. We use Model Data to estimate a 
wide range of predictive models that help us characterize home values 
in a given area. We then select the best performing models to use to 
value properties in Assessment Data.
'''

# https://datacatalog.cookcountyil.gov/resource/5pge-nu6u.json

# fields description:
# https://www.opendatanetwork.com/dataset/datacatalog.cookcountyil.gov/5pge-nu6u
# PIN explanation: https://www.cookcountyclerk.com/service/about-property-index-number-pin


'''
Assessment Data
Where Model Data is a data set of sales, Assessment Data is a data set 
of properties, even ones that have not sold in a long time. Because 
these properties still need to be valued, we use the best performing 
models from Model Data to estimate the market value for the properties 
contained within the Assessment Data table.
'''

#https://datacatalog.cookcountyil.gov/resource/bcnq-qi2z.json
# fields description:
# https://www.opendatanetwork.com/dataset/datacatalog.cookcountyil.gov/bcnq-qi2z
#

'''
First Pass values
are the values upon which re-assessment notices are based. They are 
the product of our modeling process and post-modeling adjustments. 
In this data, we have provided each value at each step in the valuation 
process. Each post-modeling adjustment produces a new set of estimated 
values 2 through 7. These values, and the resulting ratios, are stored 
in Table 3, First Pass Values, which reports the estimated market values 
of properties at each stage in the process. 
First Pass Values are not final assessments. After first-pass notices 
are mailed, the assessor finalizes assessments in township order, and 
sends those assessments to the Board of Review (BOR), and then to the 
Property Tax Appeal Board. Later, changes from things like Certificates 
of Error may also change assessments.  
'''

#https://datacatalog.cookcountyil.gov/resource/x88m-e569.json
# Fields:
# https://www.opendatanetwork.com/dataset/datacatalog.cookcountyil.gov/x88m-e569

'''
Now is the appeals stage. As I understand the corrections will be in the
next bunch of datasets similar to (in 2010)
https://datacatalog.cookcountyil.gov/resource/qh99-2dvn.json 
'''

# The description of fields in Model Data is best here:
# https://www.opendatanetwork.com/dataset/datacatalog.cookcountyil.gov/5pge-nu6u