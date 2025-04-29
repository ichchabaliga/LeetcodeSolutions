# Last updated: 29/04/2025, 19:18:58

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDiameter=0
        
    # dfs, which returns the max height
    def dfs(self,root):
        if not root:
            return 0
        left=self.dfs(root.left)
        right=self.dfs(root.right)
        diameter = right+left
        self.maxDiameter=max(diameter,self.maxDiameter)
        return 1+max(left,right)
       
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxDiameter