def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()

        def helper(start, subset, target):
            if target == 0:
                ans.append(subset[:])
                return 

            for i in range(start, n):
                if start < i and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                subset.append(candidates[i])
                helper(i + 1, subset, target - candidates[i])
                subset.pop()

        ans = []
        helper(0, [], target)

        return ans 