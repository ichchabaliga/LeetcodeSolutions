# Last updated: 30/04/2025, 21:21:54
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hasmap=defaultdict(list)
        # key would be a tuple of length 26 
        for st in strs:
            charList=[0]*26
            for char in st:
                charList[ord(char)-ord('a')]+=1
            hasmap[tuple(charList)].append(st)
        print(hasmap.values())
        return list(hasmap.values())

        