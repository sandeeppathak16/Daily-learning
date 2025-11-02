

def unique_paths(m: int, n: int) -> int:
    # Recursion
    def recursion(m, n):
        if m == 0 and n == 0:
            return 1

        if m < 0 or n < 0:
            return 0

        return recursion(m - 1, n) + recursion(m, n - 1)

    # Memoization
    def memoization(m, n, dp):
        if m == 0 and n == 0:
            return 1

        if m < 0 or n < 0:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]

        dp[m][n] = memoization(m - 1, n, dp) + memoization(m, n - 1, dp)

        return dp[m][n]

    # Tabulization
    def tabulization(dp):
        for i in range(n):
            dp[i][0] = 1

        for j in range(m):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


    # return recursion(m - 1, n - 1)
    dp = [[-1] * m for _ in range(n)]
    # return memoization(m - 1, n - 1, [[-1] * m for _ in range(n)])
    return tabulization(dp)


print(unique_paths(3, 7))


