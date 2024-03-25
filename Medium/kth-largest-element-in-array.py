from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


sol = Solution()
sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
