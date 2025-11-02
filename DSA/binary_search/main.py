def binary_search(list, target):
    ind0 = 0
    indn = len(list) - 1

    while ind0 <= indn:
        m = (ind0 + indn) // 2
        if target == list[m]:
            return m
        elif target > list[m]:
            ind0 = m + 1
        else:
            indn = m - 1
    if ind0 > indn:
        if list[ind0] == target:
            return ind0


list = [2, 7, 19, 34, 53, 72]

print(binary_search(list, 72))
