# Last updated: 29/04/2025, 20:51:23
# mid+left+right>=2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=None
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            def dfs(node):
                if not node:
                    return False
                left=dfs(node.left )
                right=dfs(node.right)
                mid = node.val==p.val or node.val==q.val
                if mid+left+right>=2:
                   self.ans = node
                return mid or left or right
            dfs(node)
            return  self.ans
