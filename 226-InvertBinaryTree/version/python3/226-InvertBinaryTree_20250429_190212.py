# Last updated: 29/04/2025, 19:02:12
# easy recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        right=self.invertTree(root.right)
        left=self.invertTree(root.left)
        root.right=left
        root.left=right
        return root
        
        
        