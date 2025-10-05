def reverse_list(list, i, j):
    if i > j:
        return

    list[i], list[j] = list[j], list[i]

    i += 1
    j -= 1

    reverse_list(list, i, j)


nums = [1, 2, 3, 4, 5]

reverse_list(nums, 0, 4)

print(nums)


