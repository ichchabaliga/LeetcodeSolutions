# Last updated: 06/06/2025, 10:42:00
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list for courses and their prerequisites
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()  # Tracks nodes in current DFS path

        def dfs(course):
            if course in visited:      # Cycle detected
                return False
            if not graph[course]:      # No prerequisites left
                return True

            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []         # Mark as completed
            return True

        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
