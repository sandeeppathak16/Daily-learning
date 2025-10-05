def print_all_subsequences(list, i, n, sq):
    if i >= n:
        print(sq)
        return

    sq.append(list[i])
    print_all_subsequences(list, i + 1, n, sq)

    sq.pop()
    print_all_subsequences(list, i + 1, n, sq)


print_all_subsequences([3, 1, 2], 0, 3, [])