def house_robber(l):
    # Recursion

    def recursion(n):

        if n == 0:
            return l[0]

        if n < 0:
            return 0

        pick = l[n] + recursion(n - 2)
        not_pick = recursion(n - 1)

        return max(pick, not_pick)

    # return recursion(len(l) - 1)

    # Memoization

    def memoization(n, dp):

        if n == 0:
            return l[0]

        if n < 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        pick = l[n] + recursion(n - 2)
        not_pick = recursion(n - 1)

        dp[n] = max(pick, not_pick)

        return dp[n]

    # return memoization(len(l) - 1, [-1 for _ in range(len(l))])
    #
    # # Tabulization
    #
    def tabulization(n):

        dp = [-1] * (n + 1)

        dp[0] = l[0]
        dp[1] = max(l[0], l[1])

        for i in range(2, n + 1):
            dp[i] = max(l[i] + dp[i - 2],  dp[i - 1])

        return dp[n]

    return tabulization(len(l) - 1)


n = [2,7,9,3,1]


print(house_robber(n))

