from typing import Any

import copy


class ListNode:
    def __init__(self, val: int = 0, next: Any = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        nodes_arr = []
        while head:
            new_node = ListNode(head.val)
            nodes_arr.append(new_node)
            head = head.next
        nodes_arr = nodes_arr[::-1]
        for i in range(len(nodes_arr) - 1):
            nodes_arr[i].next = nodes_arr[i + 1]
        return nodes_arr[0]

