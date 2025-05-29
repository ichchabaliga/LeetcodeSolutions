# Last updated: 28/05/2025, 20:08:36
'''
Wow!!!! amazong question.
use a boolean value to set direction.
if true append to end, if false append curr_node value to head.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        left_to_right=True
        level_queue=deque()
        main_queue=deque([root])
        
        while main_queue:
            queueSize=len(main_queue)
           
            
            for i in range(queueSize):
                curr_node=main_queue.popleft()
                if left_to_right:
                    level_queue.append(curr_node.val)
                   
                else:
                    level_queue.appendleft(curr_node.val)

                if curr_node.left:
                    main_queue.append(curr_node.left)
                if curr_node.right:
                    main_queue.append(curr_node.right)

            result.append(list(level_queue))
            level_queue=deque()
            left_to_right=not left_to_right
        return result
