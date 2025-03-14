# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumList=ListNode(0)
        carry=0
        curr=sumList
        while l1 or l2 or carry:
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            sumval = l1val+l2val+carry
            carry= sumval//10
            new=ListNode(sumval%10)
            curr.next=new
            curr=new
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return sumList.next


