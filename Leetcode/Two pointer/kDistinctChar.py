def kDistinctChar(s, k):
    i = 0
    mapp = {}
    ans = 0

    for j in range(len(s)):
        mapp[s[j]] = mapp.get(s[j], 0) + 1

        while len(mapp) > k:
            mapp[s[i]] -= 1
            if mapp[s[i]] == 0:
                del mapp[s[i]]

            i += 1

        ans = max(ans, j - i + 1)

    return ans
