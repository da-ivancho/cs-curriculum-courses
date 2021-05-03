def polysum(n, s):
    '''
    n: number of sides of the polygon
    s: length of each side
    returns the sum of the area and square of the permiter of a regular polygon
    '''
    import math
    areaOfPolygon = 0.25 * n * s**2 / math.tan(math.pi / n)
    perimeterOfPolygon = (n * s)**2

    return round(areaOfPolygon + perimeterOfPolygon, 4)

# Test Cases
print(polysum(56, 20))
print(polysum(87, 23))
print(polysum(60, 2))