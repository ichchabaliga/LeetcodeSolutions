# Last updated: 07/05/2025, 19:41:06
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def build_permutations(currentPerms,remainingNums):
            if not remainingNums:
                result.append(currentPerms)
                return 

            for i in range(len(remainingNums)):
                num=remainingNums[i]
                newCurrent=currentPerms+[num]
               
                newRemaining=remainingNums[:i]+remainingNums[i+1:]
                print(newRemaining)

                build_permutations(newCurrent,newRemaining)  

        build_permutations([],nums)      
        return result