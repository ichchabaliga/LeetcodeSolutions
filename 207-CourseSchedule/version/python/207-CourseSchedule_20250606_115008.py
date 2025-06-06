# Last updated: 06/06/2025, 11:50:08
class Solution:
    def canFinish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list for courses and their prerequisites
        course_graph={i:[] for i in range(num_courses)} 
        for i, prereq in prerequisites:
            course_graph[i].append(prereq)
        # Tracks nodes in current DFS path
        visit=set()

        def dfs(course):
            if course in visit:
                return False
            if not course_graph[course]:
                return True
            visit.add(course)
            for pre_req in course_graph[course]:
                if not dfs(pre_req):
                    return False
            visit.remove(course)
            course_graph[course]=[]
            return True



        for i in course_graph:
            if not dfs(i):
                return False
        return True

      

        # Check all courses
        
