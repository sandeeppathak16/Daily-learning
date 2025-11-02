def permute(nums):
    nums.sort()
    ans = []
    p = []
    frq = [False] * len(nums)

    def help_permutations():
        if len(p) == len(nums):
            ans.append(p[:])
            return

        for i in range(len(nums)):
            if frq[i] or (i > 0 and nums[i] == nums[i - 1] and not frq[i - 1]):
                continue

            p.append(nums[i])
            frq[i] = True
            help_permutations()
            p.pop()
            frq[i] = False

    help_permutations()

    return ans


print(permute([1, 1, 2]))
