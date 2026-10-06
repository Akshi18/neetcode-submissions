# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle (slow ends at middle)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # cut the list in two
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merge alternately
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2