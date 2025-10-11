def exchange(a,b):
    a = a ^ b
    b = a ^ b
    a= a ^ b
    return a , b
print(exchange(5,10))