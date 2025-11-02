def merge_sort(list_l):
    l = len(list_l)

    if l <= 1:
        return list_l

    mid = l // 2
    left = list_l[:mid]
    right = list_l[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    l = len(left)
    r = len(right)
    sorted_list = []
    i = j = 0

    while i < l and j < r:
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1
    while i < l:
        sorted_list.append(left[i])
        i += 1
    while j < r:
        sorted_list.append(right[j])
        j += 1
    return sorted_list


l = [2, 6, 11, 19, 27, 31, 45, 121]

l = merge_sort(l)
print(l)
