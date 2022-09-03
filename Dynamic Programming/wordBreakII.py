class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s,wordDict,{})
    
    
    def helper(self, s:str, wordDict: List[str], memo):
        #edge/ base
        if s in memo: return memo[s]
        
        if not s: return []
        
        res = []
        
        for w in wordDict:
            if not s.startswith(w):
                continue
            
            if len(w) == len(s):
                res.append(w)
                
            else:
                remwords = self.helper(s[len(w):], wordDict, memo)
                for subword in remwords:
                    subword = w + " " + subword
                    res.append(subword)
                    
        memo[s] = res
        return res
