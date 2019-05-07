"""
Dealing with the socrata "Floating Timestamp" datatype, the idiots added
their idiotic 'T' between the date and the time, simple str() of a datetime
format will not be enough. Thank you, idiots!
"""

import datetime as dt
from dateutil.parser import parse

datet = parse('2011-01-03T01:02:01')
backs = datet.strftime('%Y-%m-%dT%H:%M:%S')

in_a_query = f"where={backs!r}"

print(in_a_query)

yea = 2014
mon = 12
day = 1
hou = 22
mi  = 13
sec = 13
da = dt.datetime(year=yea, month=mon, day=day, hour=hou, minute=mi, second=sec)

print('ok')
