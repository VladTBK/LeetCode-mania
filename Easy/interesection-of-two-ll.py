from typing import Any, Optional


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


class Solution:
    def walkLL(self, node: ListNode, arr: list[int]) -> None:
        if not node:
            return
        arr.append(node.val)
        node = node.next  # type:ignore

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        first_ll: list[int] = []
        second_ll: list[int] = []
        self.walkLL(headA, first_ll)
        self.walkLL(headB, second_ll)
        set_first_ll = set(first_ll)
        set_second_ll = set(second_ll)
        if set_first_ll ^ set_second_ll:
            return ListNode((set_first_ll ^ set_second_ll).pop())
        else:
            return None
