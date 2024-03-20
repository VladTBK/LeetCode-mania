from typing import Optional, Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        leng = 0
        first_head = head
        while head:
            head = head.next
            leng += 1
        leng -= n
        head = first_head
        if leng == 0:
            return head.next
        idx = 0
        first_head = prev_head = head
        while head:
            if idx == leng:
                prev_head.next = head.next
                break
            idx += 1
            prev_head = head
            head = head.next
        return first_head
