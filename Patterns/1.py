# 1.
for i in range(9, 0, -1):
    for j in range(9,0,-1):
        if ((i+j) >= 9) and (i < j):
            print("*",end="") 
        else:
            print(" ",end=" ")
    print("")