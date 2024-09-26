# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        maxS = 0
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            last = stack.pop()
            s = curr.val + last
            maxS = max(s, maxS)
            curr = curr.next

        return maxS
            