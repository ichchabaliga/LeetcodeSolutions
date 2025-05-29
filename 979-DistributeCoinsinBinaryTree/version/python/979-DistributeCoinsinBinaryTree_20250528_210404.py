# Last updated: 28/05/2025, 21:04:04
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves=0
        def dfs(current):
            if not current:
                return 0
            leftcoins=dfs(current.left)
            rightcoins=dfs(current.right)
            self.moves+=abs(leftcoins)+abs(rightcoins)
            return (current.val-1) + leftcoins + rightcoins      
        dfs(root)
        return self.moves
