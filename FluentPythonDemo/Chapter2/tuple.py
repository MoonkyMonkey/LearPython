t = (20, 8)
quotient,remainder = divmod(*t)
print(quotient, remainder)


# py3 中使用 * 来处理剩余元素

a, b, *rest = range(5)
print(a, b, rest)

metro_arears = [
    ('Tokyo', 'JP', 36.933, (35.677897, 139.768676)),
    ('NewYorkNewark', 'US', 20.933, (11.677897, -
    133.768676)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_arears:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.333444, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
print(tokyo[3])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.43443, 77.323323))
delhi = City._make(delhi_data)
print(delhi)
for key, value in delhi._asdict().items():
    print(key + ':', value)

