def print_subsequences_whose_sum_is_K(lst, i, current_sum, target, n, sq):
    if i >= n:
        if current_sum == target:
            print(sq)
        return

    sq.append(lst[i])
    print_subsequences_whose_sum_is_K(lst, i + 1, current_sum + lst[i], target, n, sq)

    sq.pop()
    print_subsequences_whose_sum_is_K(lst, i + 1, current_sum, target, n, sq)


print_subsequences_whose_sum_is_K([3, 1, 2], 0, 0, 3, 3, [])
