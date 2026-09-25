def get_height(grid):
    row = len(grid)
    col = len(grid[0])

    heights = []
    for c in range(col):
        h = -1
        for r in range(row):
            if grid[r][c] == '.':
                heights.append(h)
                break

            h += 1

    return heights

def solve(filename='25.txt'):
    with open(filename, 'r') as f:
        data = f.read()

    data = data.split('\n\n')

    keys = []
    locks = []

    for d in data:
        d = list(map(list, d.split('\n')))
        first_row = d[0]
        last_row = d[len(d) - 1]

        if first_row == ['#' for _ in range(len(first_row))] and last_row == ['.' for _ in range(len(last_row))]:
            locks.append(d)
        else:
            keys.append(d)

    ans = 0

    for lock in locks:
        lock_heighs = get_height(lock)

        for key in keys:
            key_heighs = get_height(key[::-1])

            fit = True

            for i in range(5):
                if lock_heighs[i] + key_heighs[i] > 5:
                    fit = False
                    break

            if fit:
                ans += 1


    return ans