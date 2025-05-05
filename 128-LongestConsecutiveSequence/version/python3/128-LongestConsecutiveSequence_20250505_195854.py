# Last updated: 05/05/2025, 19:58:54
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longest=0
        for n in hashset:
            if (n-1) not in hashset:
                length=1
                currNum=n

                while currNum+1 in hashset:
                    length+=1
                    currNum+=1
                longest=max(longest,length)
        return longest

