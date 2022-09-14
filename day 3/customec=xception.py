class Error(Exception):
    """Base Class for other classes"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input is too large"""
    pass
key = 10

while True:
    try:
        i = int(input("Enter a number"))
        if i < key:
            raise ValueTooSmallError
        elif i > key:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value is too small")
        print("\r")
    except ValueTooLargeError:
        print("Value is too large")
        print()

print("Congo Now Go play MPL")
    