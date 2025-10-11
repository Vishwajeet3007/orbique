def feb_sequence(n):
    if n <= 1:
        return n
    else:
        return feb_sequence(n-1)+ feb_sequence(n-2)
print(feb_sequence(10))
        