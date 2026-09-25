

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(i, subset):
            if i == len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[i])
            helper(i + 1, subset)

            subset.pop()

            helper(i + 1, subset)

        helper(0, [])
        return ans
        