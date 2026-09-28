def checkSubsequenceSum(self, nums, k):
    n = len(nums)
    def helper(i, _sum):
        if i >=  n or _sum > k:
            return False
            
        if _sum == k:
            return True

        
        _sum += nums[i]

        taken = helper(i + 1, _sum)

        _sum -= nums[i]

        not_taken = helper(i + 1, _sum)

        return taken or not_taken


    return helper(0, 0)