from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            if curr_sum >= max_sum:
                max_sum = curr_sum

        return max_sum / k


sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
