def min_falling_path_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def recursion(row, col):

        if row == rows:  # Out of bounds (past the last row)
            return float('inf')
        if col < 0 or col >= cols:  # Out of bounds (columns)
            return float('inf')
        if row == rows - 1:  # Base case (last row)
            return matrix[row][col]

        return matrix[row][col] + min(recursion(row + 1, col - 1), recursion(row + 1, col), recursion(row + 1, col + 1))

    # return min(recursion(0, col) for col in range(cols))

    def memoization(row, col, dp):
        if row == rows:  # Out of bounds (past the last row)
            return float('inf')
        if col < 0 or col >= cols:  # Out of bounds (columns)
            return float('inf')
        if row == rows - 1:  # Base case (last row)
            return matrix[row][col]

        if dp[row][col] != -1:
            return dp[row][col]

        dp[row][col] = matrix[row][col] + min(recursion(row + 1, col - 1), recursion(row + 1, col), recursion(row + 1, col + 1))

        return dp[row][col]

    # memoization_dp = [[-1] * cols for _ in range(rows)]
    # return min(memoization(0, col, memoization_dp) for col in range(cols))

    # Tabulization
    def tabulization():
        dp = [[0] * cols for _ in range(rows)]

        for col in range(cols):
            dp[rows - 1][col] = matrix[rows - 1][col]

        for row in range(rows - 2, -1, -1):
            for col in range(cols):
                if col - 1 < 0:
                    ld = float('inf')
                else:
                    ld = dp[row + 1][col - 1]

                if col + 1 >= cols:
                    rd = float('inf')
                else:
                    rd = dp[row + 1][col + 1]

                dp[row][col] = matrix[row][col] + min(ld, dp[row + 1][col], rd)

        return min(dp[0])

    return tabulization()


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
print(min_falling_path_sum(matrix))
