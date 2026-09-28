class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        n = len(nums)

        def helper(i, _sum):
            if _sum == k:
                return 1

            if i == n or _sum > k:
                return 0

            
            _sum += nums[i]

            taken = helper(i + 1, _sum)

            _sum -= nums[i]

            not_taken = helper(i + 1, _sum)

            return taken + not_taken

        return helper(0, 0)


        