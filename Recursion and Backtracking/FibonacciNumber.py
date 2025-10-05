def fibonacci_number(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    return fibonacci_number(num - 1) + fibonacci_number(num - 2)


n = 5
print(f"Fibonacci number at position {n} is {fibonacci_number(n)}")