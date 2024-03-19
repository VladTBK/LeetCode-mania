import math
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maxi = -1
        for i in range(len(nums)):
            temp = 0
            try:
                idx = i
                while 1:
                    temp += nums[idx]
                    idx += 2
            except IndexError:
                maxi = max(maxi, temp)
                continue

        return maxi


sol = Solution()
print(sol.rob([2, 1, 1, 2]))
