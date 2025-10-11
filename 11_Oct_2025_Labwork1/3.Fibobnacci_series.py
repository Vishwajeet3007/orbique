def fibonacci_sequence(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    if n <=1 :
        return n
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp
print(fibonacci_sequence(10))