def triangle(tri):
    n = len(tri)

    # Recursion
    def recursion(row, col):
        if row == n - 1:
            return tri[row][col]

        down = tri[row][col] + recursion(row + 1, col)
        diagonal = tri[row][col] + recursion(row + 1, col + 1)

        return min(down, diagonal)

    # Memoization
    def memoization(row, col, dp):
        if row == n - 1:
            return tri[row][col]

        if dp[row][col] != -1:
            return dp[row][col]

        down = tri[row][col] + recursion(row + 1, col)
        diagonal = tri[row][col] + recursion(row + 1, col + 1)

        dp[row][col] = min(down, diagonal)

        return dp[row][col]

    # Tabulization
    def tabulization():
        dp = [[0] * n for _ in range(n)]
        for col in range(n):
            dp[n - 1][col] = tri[n - 1][col]

        for row in range(n - 2, -1, -1):
            for col in range(row, -1, -1):
                dp[row][col] = tri[row][col] + min(dp[row + 1][col], dp[row + 1][col + 1])

        return dp[0][0]


    # return recursion(0, 0)
    # memoization_dp = [[-1] * n for _ in range(n)]
    # return memoization(0, 0, memoization_dp)
    return tabulization()


tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(triangle(tri))
