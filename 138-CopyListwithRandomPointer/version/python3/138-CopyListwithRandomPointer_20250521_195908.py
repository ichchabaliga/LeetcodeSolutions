# Last updated: 21/05/2025, 19:59:08
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited={}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        newNode=Node(head.val,None,None)
        self.visited[head]=newNode
        newNode.next=self.copyRandomList(head.next)
        newNode.random=self.copyRandomList(head.random)
        return newNode
        