def print_name_n_time(name, count, n):
    if count >= n:
        return

    print(name)
    count += 1
    print_name_n_time(name, count, n)


print_name_n_time('sandeep', 0, 5)
