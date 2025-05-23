# Last updated: 30/04/2025, 21:07:55
# Linear search o(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        for i in range(len(intervals)):
            
                
            if newInterval[1]<intervals[i][0]:
                result.append(newInterval)
                return result+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        result.append(newInterval)
        return result
        