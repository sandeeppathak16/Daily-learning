def generateBinaryStrings(self, n):
    ans = []

    def helper(pos, last_one, s):
        if pos == n:
            ans.append(s)
            return

        helper(pos + 1, False, s + '0')

        if not last_one:
            helper(pos + 1, True, s + '1')

    helper(0, False, "")
    return ans