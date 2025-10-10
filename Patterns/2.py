for i in range(1,10):
    for j in range(1,10):
        if ((i + j) >= 9) and (i < j):
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print("")