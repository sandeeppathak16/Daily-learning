def solveNQueens(n):
    chess = [['.' for _ in range(n)] for _ in range(n)]

    ans = []

    def is_safe(row, col):
        duprow = row
        dupcol = col
        while row >= 0 and col >= 0:
            if chess[row][col] == 'Q':
                return False

            row -= 1
            col -= 1

        row = duprow
        col = dupcol

        while col >= 0:
            if chess[row][col] == 'Q':
                return False
            col -= 1

        row = duprow
        col = dupcol

        while row < n and col >= 0:
            if chess[row][col] == 'Q':
                return False

            row += 1
            col -= 1

        return True

    def place_q(col):
        if col == n:
            ans.append([''.join(row) for row in chess])
            return

        for row in range(n):
            if is_safe(row, col):
                chess[row][col] = 'Q'
                place_q(col + 1)
                chess[row][col] = '.'

    place_q(0)

    return ans