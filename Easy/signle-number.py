from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        discovered = {}

        for num in nums:
            if num not in discovered:
                discovered[num] = 0
            else:
                discovered[num] += 1

        for key in discovered:
            if discovered[key] == 0:
                return key


sol = Solution()
print(sol.singleNumber([1, 1, 2, 3, 3]))
