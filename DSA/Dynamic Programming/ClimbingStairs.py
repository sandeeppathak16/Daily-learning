def climbStairs(self, n: int) -> int:
    # def start_climbStairs(i):
    # if i == n:
    # return 1
    # if i > n:
    # return 0

    # return start_climbStairs(i + 1) + start_climbStairs(i + 2)

    # return start_climbStairs(0)

    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]