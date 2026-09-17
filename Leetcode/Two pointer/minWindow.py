def minWindow(self, s: str, t: str) -> str:
    from collections import Counter, defaultdict

    t_ct = Counter(t)

    window = defaultdict(int)

    i, j = 0, 0
    n = len(s)
    have = 0
    need = len(t_ct)
    min_len = float('inf')
    res = [-1, -1]


    while j < n:
        window[s[j]] += 1

        if s[j] in t_ct and window[s[j]] == t_ct[s[j]]:
            have += 1

        while have ==  need:
            if (j - i + 1) < min_len:
                res = [i, j]
                min_len = j - i + 1

            window[s[i]] -= 1
            if s[i] in t_ct and window[s[i]] < t_ct[s[i]]:
                have -= 1

            i += 1

        j += 1

    l, r = res
    return s[l:r+1] if min_len != float("inf") else ""



        