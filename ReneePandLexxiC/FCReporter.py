
def main():
    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    return fcName

def test_getFeatureTypeFromName():
    # Returns Point
    fcName = 'Ottawa_PNT'
    expected = '_PNT'
    actual = fcName.strip('Ottawa')
    if expected == actual:
        print 'Feature class = POINT'
    else:
        print 'Feature class = UNKNOWN'

    # Returns Line
    fcName = 'Highway_LIN'
    expected = '_LIN'
    actual = fcName.strip('Highway')
    if expected == actual:
        print 'Feature class = LINE'
    else:
        print 'Feature class = UNKNOWN'

    # Returns Polygon
    fcName = 'Ottawa_PLY'
    expected = '_PLY'
    actual = fcName.strip('Ottawa')
    if expected == actual:
        print 'Feature class = POLYGON'
    else:
         print 'Feature class = UNKNOWN'

if __name__ == '__main__':
    main()
