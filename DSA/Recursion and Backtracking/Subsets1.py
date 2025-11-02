def subsets(nums):
    def help_subsets(i, nums, n, subset, ans):
        if i == n:
            ans.append(list(subset))  # Use list() to make a copy of the list
            return

        # Include nums[i] in the current subset
        subset.append(nums[i])
        help_subsets(i + 1, nums, n, subset, ans)

        # Exclude nums[i] from the current subset
        subset.pop()
        help_subsets(i + 1, nums, n, subset, ans)

    ans = []
    help_subsets(0, nums, len(nums), [], ans)

    return ans

