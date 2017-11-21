
fmt = "Expected: {}\tActual  : {}"

def main():
## test_hasXcode()
## test_getXcodePosition()
 test_getPatternPosition()

#Exercise one - function one
def hasXcode(inText):
    return "T" in inText

def test_hasXcode():
    expected = 'True'
    actual = hasXcode('Tx6op3')
    if expected == actual:
        print 'hasXcode(Tx6op3) passed'
    else:
        print fmt.format(expected, actual)

#Excercise Two - Function 2

def getXcodePosition(inText):
    return inText.find('b')

def test_getXcodePosition():
    #Pattern does not exist
    expected = 1
    actual = getXcodePosition('Tx6op3')
    if expected == actual:
        print 'Passed: getXcodePosition is at 1'
    else:
        print fmt.format(expected, actual)

#Exercise 3 - function 3

def getPatternPosition(pattern, inText):
    pass

def test_getPatternPosition():
    # Pattern does not exist, return -1
    inText = 'Twinkle twinkle little star how I wonder what you are'
    pattern = 'little star'
    expected = -1

    actual = getPatternPosition(pattern, inText)
    if expected == actual:
        print 'Passed: getPatternPosition with pattern does not exist'
    else:
        print fmt.format(expected, actual)

    # Pattern at beginning of inText
    inText = 'abc'
    pattern = 'a'
    expected = 1

    actual = getPatternPosition(pattern, inText)
    if expected == actual:
        print 'Passed: getPatternPosition with pattern as first character'
    else:
        print fmt.format(expected, actual)

    # Pattern in middle of inText


if __name__ == '__main__':
    main()