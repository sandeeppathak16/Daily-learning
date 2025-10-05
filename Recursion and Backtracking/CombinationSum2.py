def combination_sum2(candidates, target):

    ans = []

    def combination_sum_helper(candidates, i, target, l):
        if target == 0:
            ans.append(l[:])
            return

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue

            if candidates[j] > target:
                break

            l.append(candidates[j])
            combination_sum_helper(candidates, j + 1, target - candidates[j], l)
            l.pop()

    combination_sum_helper(candidates, 0, target, [])

    return ans


nums = [10, 1, 2, 7, 6, 1, 5]
nums.sort()

print(combination_sum2(nums, 8))
