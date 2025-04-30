# Last updated: 30/04/2025, 12:13:05
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.noOfGoodNodes=0
    
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs( node, maxSofar):
            if node.val>=maxSofar:
                self.noOfGoodNodes+=1
            if node.right:
                dfs(node.right,max(node.val,maxSofar))
                
            if node.left:
                dfs(node.left,max(node.val,maxSofar))
        dfs(root,float('-inf'))
        return self.noOfGoodNodes
        
        