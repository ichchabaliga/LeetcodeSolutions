# Last updated: 06/05/2025, 19:27:00
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempNode=ListNode()
        currNode=tempNode
        while l1 and l2:
            if l1.val<l2.val:
                currNode.next=l1
                l1=l1.next
                currNode=currNode.next
            else:
                currNode.next=l2
                l2=l2.next
                currNode=currNode.next

        while l1:
            currNode.next=l1
            l1=l1.next
            currNode=currNode.next
        while l2:
            currNode.next=l2
            l2=l2.next
            currNode=currNode.next
        return tempNode.next