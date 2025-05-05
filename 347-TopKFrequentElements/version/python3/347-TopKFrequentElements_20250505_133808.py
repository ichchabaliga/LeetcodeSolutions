# Last updated: 05/05/2025, 13:38:08
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        listNums= [(-value,key) for key,value in counter.items()]
        heapify(listNums)
        result=[]
        while k :
            result.append(heappop(listNums)[1])
            k-=1
        return result


        

        

