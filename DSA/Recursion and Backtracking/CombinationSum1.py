def combination_sum(candidates, target):

    ans = []

    def combination_sum_helper(candidates, i, target, l):
        if target == 0:
            ans.append(l[:])
            return
        if i >= len(candidates) or target < 0:
            return

        l.append(candidates[i])
        combination_sum_helper(candidates, i, target - candidates[i], l)

        l.pop()
        combination_sum_helper(candidates, i + 1, target, l)

    combination_sum_helper(candidates, 0, target, [])

    return ans


print(combination_sum([2, 3, 6, 7], 7))
