# Last updated: 05/06/2025, 19:48:35
class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        def get_next(n):
            total_sum=0
            while n>0:
                n,digit=n//10,n%10
                total_sum+= digit**2
            return total_sum
        while n!=1 and n not in seen:
            seen.add(n)
            n=get_next(n)
        return n==1