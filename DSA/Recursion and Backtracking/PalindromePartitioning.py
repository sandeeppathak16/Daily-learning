def partition(s):
    def is_palindrome(start, end):
        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    ans = []
    substr = []

    def help_partition(indx):
        if indx == len(s):
            ans.append(substr[:])
            return

        for i in range(indx, len(s)):
            if is_palindrome(indx, i):
                substr.append(s[indx:i + 1])
                help_partition(i + 1)
                substr.pop()

    help_partition(0)
    return ans