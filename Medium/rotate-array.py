from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        len_arr = len(nums)
        rors = k % len_arr
        temp_val = -1
        what_to_add = []
        for _ in range(rors):
            temp_val = nums.pop()
            what_to_add.append(temp_val)
        nums[:] = what_to_add[::-1] + nums


sol = Solution()
sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
