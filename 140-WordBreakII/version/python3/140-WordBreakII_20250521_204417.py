# Last updated: 21/05/2025, 20:44:17
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        self.word_set=set(wordDict)
        self.results=[]
        self.s=s
        self.current_sentence= []
        self.bactrack(self.current_sentence,0)
        return self.results
    
    def bactrack(self,current_sentence,start):
        if start == len(self.s):
            self.results.append(" ".join(current_sentence))
            return 
        for end in range(start+1,len(self.s)+1):
            if self.s[start:end] in self.word_set:
                current_sentence.append(self.s[start:end])
                self.bactrack(current_sentence,end)
                current_sentence.pop()

        



        

        