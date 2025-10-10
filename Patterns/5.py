for i in range(30):
    for j in range(30):
        if i == 0 or i == 9 or j == 0 or j == 9 or i == j or i + j == 9:
            
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")