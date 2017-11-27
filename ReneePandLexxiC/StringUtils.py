fmt = "Expected: {}\tActual  : {}"

def main():
    test_getInitials()

def getInitials(fullName):
    initials = '.'.join(name[0].upper() for name in fullName.split())+'.'
    return initials



def test_getInitials():
#test 1 should be John Samuel Wobbly - J.S.W.

    expected = "J.S.W."
    actual = getInitials('John Samuel Wobbly')
    if expected == actual:
        print ('passed')
    else:
        print fmt.format(expected, actual)

#test 2 should be Dylan McDermott - D.M.

    expected = "D.M."
    actual = getInitials('Dylan McDermott')
    if expected == actual:
        print ('passed')
    else:
        print fmt.format(expected, actual)

#test 3 should be Nora Young - N.Y.

    expected = "N.Y."
    actual = getInitials('Nora Young')
    if expected == actual:
        print ('passed')
    else:
        print fmt.format(expected, actual)

if __name__ == '__main__':
    main()

