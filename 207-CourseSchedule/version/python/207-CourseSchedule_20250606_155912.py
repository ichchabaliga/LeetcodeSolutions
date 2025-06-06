# Last updated: 06/06/2025, 15:59:12
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map={i:[] for i in range(numCourses)}
        for course,prerequisite in prerequisites:
            prereq_map[course].append(prerequisite)
        
        result=[]
        

        visited=set()
        local_visit=set()
        def dfs(course):
            if course in local_visit:
                return False
            if course in visited:
                return True
            
            local_visit.add(course)
            for prerequisite in prereq_map[course]:
                if not dfs(prerequisite):
                    return False
            local_visit.remove(course)
            result.append(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
    
