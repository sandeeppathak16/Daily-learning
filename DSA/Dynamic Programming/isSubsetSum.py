def is_subset_sum(arr, target):
    n = len(arr)

    # Recursion
    def recursion(i, target):
        if target == 0:
            return True

        if i == n - 1:
            return arr[n - 1] == target

        not_picked = recursion(i + 1, target)

        picked = False

        if arr[i] < target:
            picked = recursion(i + 1, target - arr[i])

        return picked or not_picked

    # return recursion(0, target)

    # Memoization
    def memoization(i, target, dp):
        if target == 0:
            return True

        if i == n - 1:
            return arr[n - 1] == target

        if dp[i][target] != -1:
            return dp[i][target]

        not_picked = memoization(i + 1, target, dp)

        picked = False

        if arr[i] < target:
            picked = memoization(i + 1, target - arr[i], dp)

        dp[i][target] = picked or not_picked

        return dp[i][target]

    # memo_dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
    # return memoization(0, target, memo_dp)

    # Tabulization
    def tabulization():
        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]

                if arr[i] <= j:
                    dp[i][j] |= dp[i - 1][j - arr[i]]

        return dp[n - 1][target]

    return tabulization()


arr = [3, 34, 4, 12, 5, 2]

target = 9

print(is_subset_sum(arr, target))
