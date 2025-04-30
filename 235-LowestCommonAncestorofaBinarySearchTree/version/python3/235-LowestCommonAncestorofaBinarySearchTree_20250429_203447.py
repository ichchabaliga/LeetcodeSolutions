# Last updated: 29/04/2025, 20:34:47
'''
since its a BST: 
if root.val<p and <q 
LCA(root.right)
if root.val>pand>q
LCA(root.left)
else:
return root
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val <p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root