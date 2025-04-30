# Last updated: 30/04/2025, 11:42:34
# level order traversal and then add last element to the array
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        result=[]

        while queue:
            length_current_queue=len(queue)
            level=[]
            for i in range(length_current_queue):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level.append(node.val)
            result.append(level[-1])
        return result


