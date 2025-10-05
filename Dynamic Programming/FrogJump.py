
result = 0


def forg_jump(i, height, dp):
    # if i == 0:
    #     return 0
    #
    # if dp[i] != -1:
    #     return dp[i]
    #
    # left = forg_jump(i - 1, height, dp) + abs(height[i] - height[i - 1])
    # right = 10e10
    #
    # if i > 1:
    #     right = forg_jump(i - 2, height, dp) + abs(height[i] - height[i - 2])
    #
    # dp[i] = min(left, right)
    #
    # return dp[i]

    dp[0] = 0

    for i in range(1, len(height)):
        left = dp[i - 1] + abs(height[i] - height[i - 1])
        right = 10e10

        if i > 1:
            right = dp[i - 2] + abs(height[i] - height[i - 2])

        dp[i] = min(left, right)

    return dp[-2]


print(forg_jump(3, [20, 30, 40, 20], [-1 for _ in range(5)]))



