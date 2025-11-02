def kth_min_jump(l, n, k):

    # Recursion

    def recursion(n):

        min_step = float('inf')

        if n == 0:
            return

        for i in range(1, k+1):
            if n - i >= 0:
                jump = recursion(n - i) + abs(l[n] - l[n-i])
                min_step = min(jump, min_step)

        return min_step

    # Memoization

    def memoization(n, dp):

        min_step = float('inf')

        if n == 0:
            return

        if dp[n] != -1:
            return dp[n]

        for i in range(1, k+1):
            if n - i >= 0:
                jump = memoization(n - i) + abs(l[n] - l[n-i])
                min_step = min(jump, min_step)

        dp[n] = min_step

        return dp[n]

    # Tabulization

    def tabulization(n, dp):

        dp[0] = 0

        for i in range(1, n):
            min_step = float('inf')

            for j in range(1, k+1):
                if i - j >= 0:
                    jump = dp[i - j] + abs(l[n] - l[n-i])
                    min_step = min(jump, min_step)

            dp[i] = min_step

        return dp[n -1]




