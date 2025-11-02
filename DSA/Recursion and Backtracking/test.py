d = [[1, 80], [2, 40], [3, 90], [4, 70], [5, 90]]

# print(sorted(d, key=lambda item: item[1]))

c = [3, 1, 5, 7, 4, 2, 9, 8, 9]

# def get_second_largest_number(nums):
#     max_ele = max(nums)
#
#     while max_ele in nums:
#         nums.remove(max_ele)
#
#     return max(nums)
#
#
# print(get_second_largest_number(c))

# class A:
#     def print_hello(self):
#         print('hello')
#
#
# class B(A):
#     def print_hello(self):
#         super().print_hello()
#         print('hi')
#
#
# b = B()
# b.print_hello()

# arr = ['a', 'b']
# n = 10
#
# ans = []
# for i in range(1, n + 1):
#     sub_ans = []
#     for ele in arr:
#         sub_ans.append(f'{ele}{i}')
#
#     ans.extend(sub_ans)
#
# print(ans)


def decorator(fun):
    def wrapper(**kwargs):
        fun(**kwargs)

    return wrapper()


even_numbers = [i for i in range(1, 101) if i%2 == 0]
even_q = {
    i: i*i*i
    for i in range(1, 101) if i%2 == 0
}
