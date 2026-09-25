def generateParenthesis(self, n: int) -> list[str]:
    res = []

    def dfs(l, r, s):
        if len(s) == 2 * n:
            res.append(s)
            return

        if l < n:
            dfs(l + 1, r, s + '(')
        
        if r < l:
            dfs(l, r + 1, s + ')')

    dfs(0, 0, '')
    
    return res