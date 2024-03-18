from typing import Optional, Any
import copy


class ListNode:
    def __init__(self, val: int = 0, next: Any = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_node = None
        need_switch = False
        if not head:
            return None
        while head.next:
            if need_switch:
                temp_node.next = head.next
                head.next = temp_node
                head = temp_node.next
                need_switch = False
            else:
                temp_node = copy.deepcopy(head)
                head.next = None
                head = temp_node.next
                need_switch = True

        return head


sol = Solution()

node1 = ListNode()
node2 = ListNode()
node1.next = node2

sol.swapPairs(node1)
