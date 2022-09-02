#memoized
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        def dfs(i):
            #check if visited and return res stored in dp[i]
            if i in dp:
                return dp[i]
            
            #if 1st char of str is 0 then decode is invalid
            if(s[i] == "0"):
                return 0
            
            #main logic
            #so we can either take the next char or just 1 char[i+1]
            res = dfs(i+1)
            
            #and we can take next 2 chars [i+2]
            if(i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
                
            #store res in dp
            dp[i] = res
            return res
                
        return dfs(0)
    
#tabulated

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        #bottm up
        for i in range(len(s)-1, -1, -1):
            if(s[i] == "0"):
                dp[i] = 0
                
            #takes upto 1 char 
            else:
                dp[i] = dp[i+1]
            
            #takes upto 2 chars
            if(i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
                
        return dp[0]
        



            
            
            
            
