
fmt = "Expected: {}\tActual  : {}"

def main():
 test_hasXcode()
 test_getXcodePosition()
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
    return inText.find('T')

def test_getXcodePosition():
    #Pattern does not exist
    expected = 1
    actual = getXcodePosition('asdfghjTx6op3')
    if expected == actual:
        print 'Passed: getXcodePosition is at 1'
    else:
        print fmt.format(expected, actual)

#Exercise 3 - function 3

def getPatternPosition(pattern, inText):
    return inText.find(pattern)

def test_getPatternPosition():
    # Pattern does not exist, return -1
    inText = 'Twinkle twinkle little star how I wonder what you are'
    pattern = 'pirate'
    expected = -1
    actual = getPatternPosition(pattern, inText)
    if expected == actual:
        print 'Passed: getPatternPosition with pattern does not exist'
    else:
        print fmt.format(expected, actual)

    # Pattern at beginning of inText
    inText = 'Twinkle twinkle little star how I wonder what you are'
    pattern = 'w'
    expected = 1
    actual = getPatternPosition(pattern, inText)
    if expected == actual:
        print 'Passed: getPatternPosition with pattern as first character'
    else:
        print fmt.format(expected, actual)

    # Pattern in middle of inText
    inText = 'Twinkle twinkle little star how I wonder what you are'
    pattern = 'star'
    expected = 23
    actual = getPatternPosition(pattern, inText)
    if expected == actual:
        print 'Passed: getPatternPosition with pattern in middle of text'
    else:
        print fmt.format(expected, actual)

if __name__ == '__main__':
    main()