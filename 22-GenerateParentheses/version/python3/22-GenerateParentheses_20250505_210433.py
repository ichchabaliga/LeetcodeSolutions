# Last updated: 05/05/2025, 21:04:33
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        def backtracking(noOfOpen,noOfClosed):
            if noOfOpen==noOfClosed==n:
                result.append("".join(stack))
                return
            if noOfOpen<n:
                stack.append('(')
                backtracking(noOfOpen+1,noOfClosed)
                stack.pop()
            if noOfClosed<noOfOpen:
                stack.append(')')
                backtracking(noOfOpen,noOfClosed+1)
                stack.pop()
        backtracking(0,0)
        return result