key = 20
while True:
    i = int(input("Guess a Number: "))
    if i < key:
        print("Value is Small")
        print("\r")
    elif i > key:
        print("Value is too large")
        print("\r")
    elif i == '\0':
        print("Hehe")
    else:
        print("Congo")
        break
