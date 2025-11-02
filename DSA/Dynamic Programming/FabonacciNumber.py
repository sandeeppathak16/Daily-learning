def fibonacci_number(num, dp):
    if num == 0:
        return 0

    if num == 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci_number(num - 1, dp) + fibonacci_number(num - 2, dp)

    return dp[n]


n = 10
print(f"Fibonacci number at position {n} is {fibonacci_number(n, [-1 for _ in range(n+1)])}")