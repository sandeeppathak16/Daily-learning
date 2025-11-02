def subsetsWithDup(nums):
    nums.sort()
    ans = []
    subset = []

    def help_subsets(indx):
        ans.append(subset.copy())

        for i in range(indx, len(nums)):
            if i != indx and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            help_subsets(i + 1)
            subset.pop()

    help_subsets(0)

    return ans