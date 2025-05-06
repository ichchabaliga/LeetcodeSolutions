# Last updated: 06/05/2025, 18:55:39
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList( self, head: Optional [ListNode] ) -> Optional[ListNode]:
        if not head: return None
        prev=None
        curr=head
        while curr:
            nextN=curr.next
            curr.next=prev
            prev=curr
            curr=nextN
        return prev
        

        