def print_any_one_subsequence_with_sum_K(lst, i, current_sum, target, sq):
    if i == len(lst):
        if current_sum == target:
            print(sq)
            return True
        return False

    sq.append(lst[i])
    if print_any_one_subsequence_with_sum_K(lst, i + 1, current_sum + lst[i], target, sq):
        return True

    sq.pop()
    if print_any_one_subsequence_with_sum_K(lst, i + 1, current_sum, target, sq):
        return True

    return False


print_any_one_subsequence_with_sum_K([3, 1, 2], 0, 0, 3, [])
