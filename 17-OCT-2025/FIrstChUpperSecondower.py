def uppereLower(name):
    for i, char in enumerate(name):
        if i % 2 == 0:
            print(char.upper(),end="")
        else:
            print(char.lower(),end="")
    print("\n")

uppereLower("vishwajeet")