# Last updated: 06/05/2025, 21:10:29
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        first,second= dummy, head
        while n>0 and second:
            second=second.next
            n-=1
        while second:
            second=second.next
            first=first.next
        first.next=first.next.next
        return dummy.next




        