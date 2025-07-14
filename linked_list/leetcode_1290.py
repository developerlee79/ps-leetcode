from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        target = head.val
        head = head.next
        while head is not None:
            target <<= 1
            target += head.val
            head = head.next
        return target
