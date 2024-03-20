from typing import List
import copy


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        key_stack = {key for key in rooms[0]}
        need_to_visit = len(rooms)
        visited = 1
        discovered = copy.deepcopy(key_stack)
        discovered.add(0)

        while key_stack:
            curr_key = key_stack.pop()
            visited += 1
            for key in rooms[curr_key]:
                if key not in discovered:
                    key_stack.add(key)
                    discovered.add(key)

        return visited == need_to_visit


sol = Solution()
print(sol.canVisitAllRooms([[1, 3], [1, 4], [2, 3, 4, 1], [], [4, 3, 2]]))
