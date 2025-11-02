def unique_paths_with_obstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[-1] * n for _ in range(m)]

    # Recursion
    def recursion(m, n):
        if m == 0 and n == 0:
            return 1 if obstacleGrid[0][0] == 0 else 0

        if m < 0 or n < 0 or obstacleGrid[m][n] == 1:
            return 0

        return recursion(m - 1, n) + recursion(m, n - 1)

    # Memoization
    def memoization(m, n, dp):
        if m == 0 and n == 0:
            return 1 if obstacleGrid[0][0] == 0 else 0

        if m < 0 or n < 0 or obstacleGrid[m][n] == 1:
            return 0

        dp[m][n] = memoization(m - 1, n, dp) + memoization(m, n - 1, dp)

        return dp[m][n]

    # Tabulization
    def tabulization(dp):

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]

    # return memoization(m - 1, n - 1, dp)
    return tabulization([[0] * n for _ in range(m)])


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(unique_paths_with_obstacles(obstacleGrid))
