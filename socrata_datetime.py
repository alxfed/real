"""
Dealing with the socrata "Floating Timestamp" datatype
"""

from dateutil.parser import parse

datet = parse('2011-01-03T01:02:01')
backs = datet.strftime('%Y-%m-%dT%H:%M:%S')

print(datet)
