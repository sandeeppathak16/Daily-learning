def myPow(x: float, n: int) -> float:
    def helper(exp):
        if exp == 0:
            return 1
        half = helper(exp // 2)
        if exp % 2 == 0:
            return half * half
        else:
            return half * half * x

    if n < 0:
        return 1 / helper(-n)
    return helper(n)