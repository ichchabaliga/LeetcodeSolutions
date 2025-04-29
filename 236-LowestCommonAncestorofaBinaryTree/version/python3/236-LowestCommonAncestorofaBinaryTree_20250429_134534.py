# Last updated: 29/04/2025, 13:45:34
'''
use 2 variables left and right. return node if node.val =p or q,or left and right.

return left if left and nor right
return right if not left and right
else return none
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not node:
                return None
            elif node.val == p.val or node.val == q.val:
                return node
            else:
                left = self.lowestCommonAncestor(node.left, p, q)
                right = self.lowestCommonAncestor(node.right, p, q)
                if left and right:
                    return node
                elif left and not right:
                    return left
                elif right and not left:
                    return right
                else:
                    return None
