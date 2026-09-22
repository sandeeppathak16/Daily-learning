def count_ways(word, patterns, max_len):
    n = len(word)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        total = 0
        for length in range(1, min(max_len, i) + 1):
            if word[i - length:i] in patterns:
                total += dp[i - length]
        dp[i] = total

    return dp[n]


def solve(filename='19.txt'):
    with open(filename, 'r') as f:
        code_input = f.read()

    pattern, matches = code_input.strip().split('\n\n')
    pattern = [p.strip() for p in pattern.strip().split(',')]
    matches = [m.strip() for m in matches.strip().split('\n')]

    patterns = set(pattern)
    max_len = max(len(p) for p in patterns)

    part1 = 0
    part2 = 0

    for m in matches:
        ways = count_ways(m, patterns, max_len)
        if ways:
            part1 += 1
            part2 += ways

    print(part1, part2)


solve()