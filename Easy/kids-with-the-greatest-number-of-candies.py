from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if not candies:
            return []
        max = -1
        for candy in candies:
            if candy >= max:
                max = candy

        return [candy + extraCandies >= max for candy in candies]


sol = Solution()
print(sol.kidsWithCandies([12, 5, 12], 7))
