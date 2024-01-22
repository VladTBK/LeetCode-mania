# Definition for singly-linked list.
def get_values(curr_list):
    val_list = []
    temp = curr_list
    while temp:
        val_list.append(temp.val)
        temp = temp.next
    return val_list


def array_to_int(curr_list):
    n = len(curr_list)
    num = 0
    for i in range(n):
        num += curr_list[i] * 10 ** (n - i - 1)
    return num


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first_list = get_values(l1)[::-1]
        second_list = get_values(l2)[::-1]
        num1 = array_to_int(first_list)
        num2 = array_to_int(second_list)
        total = num1 + num2
        total_list = [int(i) for i in str(total)][::-1]
        output_ll = []
        for i in range(len(total_list)):
            new_node = ListNode(val=total_list[i])
            output_ll.append(new_node)
        for idx, node in enumerate(output_ll):
            try:
                node.next = output_ll[idx + 1]
            except Exception:
                node.next = None
        return output_ll[0]
