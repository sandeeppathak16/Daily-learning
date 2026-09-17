from typing import List

def numberOfSubarrays(nums: List[int], k: int) -> int:
    def atmost(s):
        if s < 0:
            return 0

        i = 0
        _count = 0
        odd_count = 0

        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd_count += 1

            while odd_count > s:
                if nums[i] % 2 == 1:
                    odd_count -= 1

                i += 1

            _count += (j - i + 1)

        return _count

    return atmost(k) - atmost(k - 1)