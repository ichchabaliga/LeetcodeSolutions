# Last updated: 28/04/2025, 20:40:05
# Level order but keep track of parent
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue=deque([(root,None)])
        while queue:
            found={}
            for _ in range(len(queue)) :
                node,parent=queue.popleft()
                if node.val==x or node.val==y:
                    found[node.val]=parent
                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
            if found:
                return len(found)==2 and found[x]!=found[y]
        return False
                