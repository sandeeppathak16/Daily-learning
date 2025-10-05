def print_linearly_from_1_to_n(count, n):
    if count > n:
        return

    print(count)
    count += 1
    print_linearly_from_1_to_n(count, n)


print_linearly_from_1_to_n(1, 5)
