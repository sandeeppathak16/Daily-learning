from typing import *


def ninja_training(n: int, points: List[List[int]]) -> int:
    # Recursion
    def recursion(day, last):
        if day == n:
            return 0

        max_point = 0

        for i in range(3):
            if i != last:
                max_point = max(max_point, points[day][i] + recursion(day + 1, i))

        return max_point

    # Memoization
    def memoization(day, last, dp):
        if day == n:
            return 0

        if dp[day][last] != -1:
            return dp[day][last]

        max_point = 0
        for i in range(3):
            if i != last:
                max_point = max(max_point, points[day][i] + memoization(day + 1, i, dp))

        dp[day][last] = max_point

        return max_point

    # Tabulization

    def tabulization(dp):
        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0])

        for day in range(1, n):
            for last in range(4):
                dp[day][last] = 0
                max_point = 0

                for task in range(3):
                    if task != last:
                        max_point = max(max_point, points[day][task] + dp[day - 1][task])

                dp[day][last] = max_point

        return dp[n - 1][3]

    # return recursion(0, 3)

    dp = [[-1] * 4 for _ in range(n)]
    # return memoization(0, 3, dp)
    return tabulization(dp)


points = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]

print(ninja_training(3, points))
