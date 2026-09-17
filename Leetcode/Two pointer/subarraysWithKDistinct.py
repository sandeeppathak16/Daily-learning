from typing import List

def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atmostK(k):
        if k < 0:
            return 0

        i = 0
        freq = {}
        ans = 0

        for j in range(len(nums)):
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while len(freq) > k:
                freq[nums[i]] -= 1

                if freq[nums[i]] == 0:
                    del freq[nums[i]]

                i += 1

            ans += (j - i + 1)

        return ans

    return atmostK(k) - atmostK(k - 1)