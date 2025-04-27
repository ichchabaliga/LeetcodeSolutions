# Last updated: 27/04/2025, 12:25:06
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans=[]
        pq=[(-count,char) for char,count in Counter(s).items()]
        heapify(pq)

        while pq:
            cfirst,charFirst=heappop(pq)
            if not ans or ans[-1]!=charFirst:
                ans.append(charFirst)
                if cfirst+1!=0:
                    heappush(pq,(cfirst+1,charFirst))
            else:
                if not pq: return ""
                csecond,charSecond=heappop(pq)
                ans.append(charSecond)
                if csecond+1!=0:
                    heappush(pq,(csecond+1,charSecond))

                heappush(pq,(cfirst,charFirst))
        return ''.join(ans)
