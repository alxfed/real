"""
Dealing with the socrata "Floating Timestamp" datatype, the idiots added
their idiotic 'T' between the date and the time, simple str() of a datetime
format will not be enough. Thank you, idiots!
"""

from dateutil.parser import parse

datet = parse('2011-01-03T01:02:01')
backs = datet.strftime('%Y-%m-%dT%H:%M:%S')

in_a_query = f"where={backs!r}"

print(in_a_query)
