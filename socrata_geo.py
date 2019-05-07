"""
conversions from/to GeoJSON to WKT/WKB and back for use with socrata
https://github.com/larsbutler/geomet
"""


from geomet import wkt

point = {'type': 'Point', 'coordinates': [116.4, 45.2, 11.1]}

point_wkt = wkt.dumps(point, decimals=4)

print(point_wkt)

poly = {'type': 'Polygon',
        'coordinates': [[[0.0, 0.0]], [[10.0, 30.0]], [[30.0, 10.0]], [[0.0, 0.0]]]}

poly_wkt = wkt.dumps(poly, decimals=2)

print(poly_wkt)
