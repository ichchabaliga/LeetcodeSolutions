# Last updated: 05/05/2025, 20:47:34
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
                if t not in "+-/*":
                    stack.append(int(t))
                    continue
            
                b=stack.pop()
                a=stack.pop()
                if t=='+':
                    stack.append(a+b)
                elif t=='-':
                    stack.append(a-b)
                elif t=='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()
        