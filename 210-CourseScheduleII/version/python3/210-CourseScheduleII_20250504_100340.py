# Last updated: 04/05/2025, 10:03:40
# use cycle,visit set and output[]
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq={i:[] for i in range(numCourses)}
        for i,prerequisite in prerequisites:
            preReq[i].append(prerequisite)


        output=[]
        cycle,visit=set(),set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in preReq[course]:
                if not dfs(pre):
                    return False
            output.append(course)
            cycle.remove(course)
            visit.add(course)
            return True


        for course in range(numCourses):
            if not dfs(course): return []
        return output
