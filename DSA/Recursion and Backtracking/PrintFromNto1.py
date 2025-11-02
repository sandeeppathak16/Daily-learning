def print_linearly_from_n_to_1(count):
    if count < 1:
        return

    print(count)
    count -= 1
    print_linearly_from_n_to_1(count)


print_linearly_from_n_to_1(10)
