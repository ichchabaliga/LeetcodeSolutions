# Last updated: 05/05/2025, 20:06:57
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        mapBrackets={'}':"{",']':'[',")":"("}
        stack=[]
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if  stack and stack[-1]== mapBrackets[ch]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False

        