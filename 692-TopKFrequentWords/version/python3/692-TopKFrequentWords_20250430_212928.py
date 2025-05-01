# Last updated: 30/04/2025, 21:29:28
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        listOfWords=Counter(words)
        maxheap=[(-freq,word) for word, freq in listOfWords.items()]
        heapify(maxheap)
        result=[]
        while k:
            result.append(heappop(maxheap)[1])
            k-=1
        return result

        