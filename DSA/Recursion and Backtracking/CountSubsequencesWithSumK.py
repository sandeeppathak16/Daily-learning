def count_subsequences_with_sum_K(lst, i, current_sum, target):
    if i == len(lst):
        return 1 if current_sum == target else 0

    c1 = count_subsequences_with_sum_K(lst, i + 1, current_sum + lst[i], target)
    c2 = count_subsequences_with_sum_K(lst, i + 1, current_sum, target)

    return c1 + c2


c = count_subsequences_with_sum_K([3, 1, 2], 0, 0, 3)
print(c)
