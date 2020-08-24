# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        result_tail = res
        buf = 0
        while l1 or l2 or buf:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            buf, r = divmod(val1 + val2 + buf, 10)
            result_tail.next = ListNode(r)
            result_tail = result_tail.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return res.next
