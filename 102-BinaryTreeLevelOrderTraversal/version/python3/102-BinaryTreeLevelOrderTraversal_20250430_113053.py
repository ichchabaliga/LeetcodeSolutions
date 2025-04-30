# Last updated: 30/04/2025, 11:30:53
# use a queue and a list for each level
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        levels=[]
        while queue:
            length_current_level=len(queue)
            current_level=[]
            for i in range(length_current_level):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            levels.append(current_level)
        return levels