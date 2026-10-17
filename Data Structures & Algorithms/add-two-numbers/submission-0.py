# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        sum1 = 0
        sum2 = 0
        cur = l1
        while cur:
            sum1 = sum1 + (cur.val * (10**cnt))
            cnt+=1
            cur=cur.next

        cur = l2
        cnt = 0
        while cur:
            sum2 = sum2 + (cur.val * (10**cnt))
            cnt+=1
            cur=cur.next

        total_sum = sum1 + sum2

        if not total_sum:
            return ListNode(0)
        
        head = None
        tail = None
        while total_sum:
            digit = total_sum % 10
            total_sum = total_sum //10
            new_node = ListNode(digit)
            if not head:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node
                

        return head
            

            