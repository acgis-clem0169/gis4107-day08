
def main():
    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    if fcName.endswith(('_PNT','_pnt')):
        return 'Point'
    if fcName.endswith(('_LIN','_lin')):
        return 'Line'
    if fcName.endswith(('_PLY','_ply')):
        return 'Polygon'
    else:
        return "UNKNOWN"

def test_getFeatureTypeFromName():
    # Returns Point
    expected = 'Point'
    actual = getFeatureTypeFromName('Ottawa_PNT')
    if expected == actual:
        print 'PASSED: Feature class = POINT'
    else:
        print 'FAILED: Expected: {}\nActual: {}'.format(expected, actual)

    # Returns Line
    expected = 'Line'
    actual = getFeatureTypeFromName('Ottawa_LIN')
    if expected == actual:
        print 'PASSED: Feature class = LINE'
    else:
        print 'FAILED: Expected: {}\nActual: {}'.format(expected, actual)

    # Returns Polygon
    expected = 'Polygon'
    actual = getFeatureTypeFromName('Ottawa_PLY')
    if expected == actual:
        print 'PASSED: Feature class = POLYGON'
    else:
        print 'FAILED: Expected: {}\nActual: {}'.format(expected, actual)

if __name__ == '__main__':
    main()
