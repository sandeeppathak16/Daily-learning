from collections import deque

def all_shortest_path(src, dest, grid, rows, cols):
    queue = deque([(src, 0, '')])
    visited = {src}
    paths = {}

    mapping = {
        (0, 1): '>',
        (0, -1): '<',
        (1, 0): 'v',
        (-1, 0): '^'
    }

    while queue:
        s, ct, p = queue.popleft()

        r, c = s

        if (r, c) == dest:
            if not paths:
                paths[ct] = [p + 'A']
            elif paths and ct in paths:
                paths[ct].append(p + 'A')

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != "X"
                # and (nr, nc) not in visited
            ):
                # visited.add((nr, nc))
                new_path = p[:] + mapping[(dr, dc)]
                queue.append(((nr, nc), ct + 1, new_path))

    return next(iter(paths.values()))


def solve(filename='21.txt'):
    with open(filename, 'r') as f:
        codes = [line.strip() for line in f.readlines()]

    numeric_keypad_grid = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["X", "0", "A"]
    ]

    directional_keypad_grid = [
        [None, "^", "A"],
        ["<", "v", ">"]
    ]

    numeric_pos = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "1": (2, 0), "2": (2, 1), "3": (2, 2),
        "0": (3, 1), "A": (3, 2),
    }

    directional_pos = {
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
    }

    src = numeric_pos['A']
    paths = []

    for dest in '029A':
        next_paths = all_shortest_path(src, numeric_pos[dest], numeric_keypad_grid, 4, 3)
        print(src, numeric_pos[dest], next_paths, paths)

        if not paths:
            paths = next_paths
        else:
            new_paths = []

            for path in paths:
                for next_path in next_paths:
                    new_paths.append(path + next_path)

            paths = new_paths

        src = numeric_pos[dest]

    return paths

print(solve())



    

