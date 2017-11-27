fmt = "Expected: {}\tActual  : {}"

def main():
    test_ValidPhoneNumber()

def ValidPhoneNumber(phoneNumber):



def test_ValidPhoneNumber():
    # Test case 1
    expected = "expected value"
    actual = ValidPhoneNumber(1)
    if expected == actual:
        print "func1(1) passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()