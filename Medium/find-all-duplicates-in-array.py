from typing import List
from collections import defaultdict


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        discovered: dict[int, int] = defaultdict(int)
        for val in nums:
            if val not in discovered:
                discovered[val] += 1
        out_arr: list[int] = []
        for key, val in discovered.items():
            if val == 2:
                out_arr.append(key)
        return out_arr
