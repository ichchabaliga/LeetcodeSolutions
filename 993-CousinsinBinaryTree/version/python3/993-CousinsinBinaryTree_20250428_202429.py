# Last updated: 28/04/2025, 20:24:29
# Level order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        while queue:
            siblings = False
            cousins = False
            nodes_at_depth = len(queue)
            for _ in range(nodes_at_depth):
                node = queue.popleft()  
                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            return not siblings

                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    queue.append(None)
            if cousins:
                return False

        return False        