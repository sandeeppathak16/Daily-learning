from collections import defaultdict


def next_secret(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number


def solve(filename="22.txt"):
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]

    part1 = 0
    pattern_totals = defaultdict(int)

    for initial in numbers:
        secret = initial
        secrets = [secret]

        for _ in range(2000):
            secret = next_secret(secret)
            secrets.append(secret)

        part1 += secrets[2000]

        prices = [secret % 10 for secret in secrets]

        changes = [
            prices[i] - prices[i - 1]
            for i in range(1, len(prices))
        ]

        seen = set()

        for i in range(len(changes) - 3):
            pattern = tuple(changes[i:i + 4])

            if pattern in seen:
                continue

            seen.add(pattern)

            price = prices[i + 4]

            pattern_totals[pattern] += price

    part2 = max(pattern_totals.values())

    return part1, part2


part1, part2 = solve()

print("Part 1:", part1)
print("Part 2:", part2)