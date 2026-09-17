from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:

        i = 0
        ans = 0
        mapping = {}

        _sum = 0

        for j in range(len(nums)):
            _sum += nums[j]

            if _sum == goal:
                ans += 1

            rem = _sum - goal

            if rem in mapping:
                ans += mapping[rem]

            mapping[_sum] = mapping.get(_sum, 0) + 1

        return ans


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    def atMost(k):
        if k < 0:
            return 0
        count = 0
        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            count += right - left + 1
        return count

    return atMost(goal) - atMost(goal - 1)