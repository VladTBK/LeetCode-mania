from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        if len(nums) == 1:
            return True
        for num in nums:
            if gas < 0:
                return False
            if num > gas:
                gas = num
            gas -= 1

        return True
