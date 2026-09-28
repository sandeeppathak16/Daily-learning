class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        

        # def helper(start, subset, curr_sum):
        #     if curr_sum == target:
        #         ans.append(subset[:])
        #         return

        #     if curr_sum > target:
        #         return

        #     for i in range(start, len(candidates)):
        #         subset.append(candidates[i])
        #         helper(i, subset, curr_sum + candidates[i])  # reuse allowed
        #         subset.pop()
        # # ans = []

        # helper(0, [], 0)

        # return ans
        n = len(candidates)
        ans = []

        def helper(i, subset, curr_sum):
            if curr_sum == target:
                ans.append(subset[:])
                return 
            
            if i >= n or curr_sum > target:
                return 

            subset.append(candidates[i])
            helper(i, subset, curr_sum + candidates[i])

            subset.pop()
            helper(i + 1, subset, curr_sum)

        helper(0, [], 0)
        return ans