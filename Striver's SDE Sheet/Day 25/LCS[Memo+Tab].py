'''Memoization
Time Complexity: O(N*M)
Space Complexity: O(N*M) + AUXSS = O(N+M)'''

def f(ind1,ind2,s1,s2,dp):
	if(ind1<0 or ind2<0):
		return 0
	
	if(dp[ind1][ind2] != -1):
		return dp[ind1][ind2]
	
	if(s1[ind1] == s2[ind2]):
		dp[ind1][ind2] = 1 + f(ind1-1,ind2-1,s1,s2,dp)
		return dp[ind1][ind2]
	
	dp[ind1][ind2] = max(f(ind1-1,ind2,s1,s2,dp),f(ind1,ind2-1,s1,s2,dp))
	return dp[ind1][ind2]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for i in range(len(text2))] for i in range(len(text1))]
        return f(n-1,m-1,text1,text2,dp)



'''Tabulation
Time Complexity: O(N*M)
Space Complexity: O(N*M)'''
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        
        #iterative bottom up approach
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i] == s2[j]:
                    #matches -> move diagnlly
                    dp[i][j] = 1 + dp[i+1][j+1]
                    
                else: #do not match -> take max of right and bottom
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
