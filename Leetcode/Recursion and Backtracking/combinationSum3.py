class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        def helper(i, subset, current_sum, current_len):
            if current_len == k and current_sum == n:
                ans.append(subset[:])
                return 

            if current_len > k or current_sum > n:
                return 

            for j in range(i, 10):
                subset.append(j)
                helper(j + 1, subset, current_sum + j, current_len + 1)
                subset.pop()

        helper(1, [], 0, 0)
        return ans

        