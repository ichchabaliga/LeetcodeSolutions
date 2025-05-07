# Last updated: 06/05/2025, 20:40:25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        second=slow.next
        slow.next=None
        
        while second:  
            nextN=second.next          
            second.next=prev
            prev=second
            second=nextN

        second=prev
        first=head
        
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2

