from collections import deque
from functools import cache

NUMERIC = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["X", "0", "A"],
]

DIR = [
    ["X", "^", "A"],
    ["<", "v", ">"],
]

MOVES = [
    (0, 1, ">"),
    (0, -1, "<"),
    (1, 0, "v"),
    (-1, 0, "^"),
]

NUM_POS = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2),
}

DIR_POS = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def all_shortest_paths(start, end, grid):
    rows, cols = len(grid), len(grid[0])

    q = deque([(start, "")])
    dist = {start: 0}

    best = None
    ans = []

    while q:
        pos, path = q.popleft()
        r, c = pos

        if best is not None and len(path) > best:
            continue

        if pos == end:
            best = len(path)

            if len(path) == best:
                ans.append(path + "A")
            continue

        for dr, dc, move in MOVES:
            nr, nc = r + dr, c + dc

            if not (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != "X"
            ):
                continue

            nd = len(path) + 1

            if nd <= dist.get((nr, nc), float("inf")):
                dist[(nr, nc)] = nd
                q.append(((nr, nc), path + move))

    return ans


NUMERIC_PATHS = {}
for a in NUM_POS:
    for b in NUM_POS:
        NUMERIC_PATHS[(a, b)] = all_shortest_paths(
            NUM_POS[a], NUM_POS[b], NUMERIC
        )

DIRECTIONAL_PATHS = {}
for a in DIR_POS:
    for b in DIR_POS:
        DIRECTIONAL_PATHS[(a, b)] = all_shortest_paths(
            DIR_POS[a], DIR_POS[b], DIR
        )


@cache
def cost_between(a, b, depth):
    paths = DIRECTIONAL_PATHS[(a, b)]

    if depth == 0:
        return min(len(p) for p in paths)

    best = float("inf")

    for path in paths:
        total = 0
        prev = "A"

        for ch in path:
            total += cost_between(prev, ch, depth - 1)
            prev = ch

        best = min(best, total)

    return best


def solve_code(code, robots=25):
    total = 0
    prev = "A"

    for ch in code:
        best = float("inf")

        for path in NUMERIC_PATHS[(prev, ch)]:
            cur = 0
            p = "A"

            for x in path:
                cur += cost_between(p, x, robots - 1)
                p = x

            best = min(best, cur)

        total += best
        prev = ch

    return total


def solve(filename="21.txt", robots=25):
    ans = 0

    with open(filename) as f:
        for code in map(str.strip, f):
            presses = solve_code(code, robots)
            ans += int(code[:-1]) * presses

    return ans


print(solve(robots=25))