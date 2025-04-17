# Last updated: 16/04/2025, 20:07:57
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap={}
        for a in arr:
            hashmap[a]=hashmap.get(a,0)+1
        return len(set(hashmap.values()))==len(hashmap)