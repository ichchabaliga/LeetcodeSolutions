# Last updated: 29/04/2025, 14:33:11
'''
create a helper function to find height of left and right subtree. 
return abs(helper(node.left)-helper(node.right)) and isBalanced(node.left) and isBalanced(node.right)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node):
        if not node:
            return 0
        return 1+max(self.height(node.left),self.height(node.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return  abs((self.height(root.left) - self.height(root.right))) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)