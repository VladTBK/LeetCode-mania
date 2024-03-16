from typing import Optional, Any


class ListNode:
    def __init__(self, val: int = 0, next: Any = None) -> None:
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2

    if not list2:
        return list1

    print(list1.val)
    print(list2.val)
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


list1 = ListNode(1)
list1.next = ListNode(2)


list2 = ListNode(1)
list2.next = ListNode(3)


out_list = mergeTwoLists(list1, list2)
while out_list:
    print(out_list.val)
    out_list = out_list.next
