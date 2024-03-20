from typing import Optional, Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        old_head = head
        while head.next:  # type:ignore
            head = head.next  # type:ignore
            length += 1
        head = old_head
        runs = k % length
        for _ in range(runs):
            old_head = prev_head = head
            while head.next:  # type:ignore
                prev_head = head  # type: ignore
                head = head.next  # type:ignore
            head.next = old_head  # type:ignore
            prev_head.next = None  # type:ignore
        return head
