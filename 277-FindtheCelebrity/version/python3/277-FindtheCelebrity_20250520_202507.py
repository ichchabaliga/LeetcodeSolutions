# Last updated: 20/05/2025, 20:25:07
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n=n
        candidate=0
        for i in range(1,n):
            if knows(candidate,i):
                candidate=i

        if self.isCelebrity(candidate):
            return candidate
        return -1

    def isCelebrity(self,i):
        for j in range(self.n):
            if i==j: continue
            if knows(i,j) or not knows(j,i) :
                return False
        return True


        