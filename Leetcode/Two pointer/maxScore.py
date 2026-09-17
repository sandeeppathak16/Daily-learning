from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    ans = sum(cardPoints[:k])
    curr = ans

    for i in range(k):
        curr -= cardPoints[k - 1 - i]
        curr += cardPoints[n - 1 - i]

        ans = max(curr, ans)

    return ans