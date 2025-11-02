def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(elements, start, end):
    pivote_index = start
    pivote = elements[pivote_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivote:
            start += 1
        while elements[end] > pivote:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivote_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


ele = [11, 9, 29, 7, 2, 15, 28, 2]
quick_sort(ele, 0, len(ele) - 1)
print(ele)
