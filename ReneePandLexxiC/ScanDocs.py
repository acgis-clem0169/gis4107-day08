#-------------------------------------------------------------------------------
# Name:        Exercise 1
# Purpose:
#
# Author:      Renee and Lexxi
#
# Created:     21-11-2017
# Copyright:   (c) renny 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
fmt = "Expected: {}\tActual  : {}"

def main():
    test_hasXcode()
    test_getXcodePosition()

def hasXcode(inText):
    return "T" in inText

def test_hasXcode():
    expected = 'True'
    actual = hasXcode('Tx6op3')
    if expected == actual:
        print 'hasXcode(Tx6op3) passed'
    else:
        print fmt.format(expected, actual)

def getXcodePosition(inText):
    print inText.find('T')

def test_getXcodePosition():
      getXcodePosition('0Tx6op3')

if __name__ == '__main__':
    main()