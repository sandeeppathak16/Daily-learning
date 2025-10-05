def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])

    # Recursion
    def recursion(m, n):
        if m == 0 and n == 0:
            return grid[0][0]

        if m < 0 or n < 0:
            return float('inf')

        up = grid[m][n] + recursion(m - 1, n)
        left = grid[m][n] + recursion(m, n - 1)

        return min(up, left)

    # Memoization
    def memoization(m, n, dp):
        if m == 0 and n == 0:
            return grid[0][0]

        if m < 0 or n < 0:
            return float('inf')

        if dp[m][n] != -1:
            return dp[m][n]

        up = grid[m][n] + recursion(m - 1, n)
        left = grid[m][n] + recursion(m, n - 1)

        dp[m][n] = min(up, left)

        return dp[m][n]

    # Tabulization
    def tabulization(dp):
        for i in range(m):
            dp[i][0] = grid[i][0]

        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]

    # return recursion(m - 1, n - 1)
    # memoization_dp = [[-1] * n for _ in range(m)]
    # return memoization(m - 1, n - 1, memoization_dp)
    return tabulization([[0] * n for _ in range(m)])


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))
