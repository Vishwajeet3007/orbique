def fib(n):
    a , b = 0 , 1
    for _ in range(1,n):
        print(a , end = " ")
        a , b = b ,a + b
    print("\n")
fib(10)