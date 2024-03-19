import collections
from typing import Any, List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        discovered: dict[int, int] = collections.defaultdict(int)
        for num in nums:
            discovered[num] += 1

        max_val = 0
        max_key: int = 0
        for key, val in discovered.items():
            if val > max_val:
                max_val = val
                max_key = key

        return max_key


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


sol = Solution()
print(sol.majorityElement([3, 2, 3, 2, 2]))
