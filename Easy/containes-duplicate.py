from typing import List


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         discovered = []
#         for num in nums:
#             if num not in discovered:
#                 discovered.append(num)
#             else:

#                 return True
#         return False


# faster with dicstionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        discovered = {}
        for num in nums:
            if num not in discovered:
                discovered[num] = 0
            else:
                return True
        return False
