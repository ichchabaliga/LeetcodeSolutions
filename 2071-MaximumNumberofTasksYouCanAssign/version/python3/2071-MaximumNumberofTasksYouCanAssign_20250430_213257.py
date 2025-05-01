# Last updated: 30/04/2025, 21:32:57
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        
        def can_assign(k):
            p = pills
            available = deque()
            j = len(workers) - 1
            # Try to assign the k hardest tasks
            for i in range(k - 1, -1, -1):
                # Add workers who can do the task with a pill
                while j >= len(workers) - k and workers[j] + strength >= tasks[i]:
                    available.appendleft(workers[j])
                    j -= 1
                if not available:
                    return False
                # Assign the strongest available worker if possible
                if available[-1] >= tasks[i]:
                    available.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    available.popleft()
            return True

        left, right, answer = 1, min(len(tasks), len(workers)), 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
