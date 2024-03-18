from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        discovered = {}
        for num in nums:
            if num not in discovered:
                discovered[num] = 0
            if num in discovered:
                discovered[num] += 1
        for key in discovered:
            if discovered[key] == 1:
                return key


