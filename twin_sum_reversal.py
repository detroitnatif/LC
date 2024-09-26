# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        i = head
        maxS = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        

        prev = None
        temp = slow
        while slow:
            nx = slow.next
            slow.next = prev
            prev = slow
            slow = nx
        slowC = prev

        while slowC:
            o = i.val + slowC.val
            maxS = max(maxS, o)

            i = i.next
            slowC = slowC.next

        return maxS



            
