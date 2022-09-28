'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.
'''

'''
MEMOIZATION - TOP DOWN
TIME- O(N^2)
SPACE - O(N) + A.S.S O(N)
'''
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        dp = [-1] * n
        
        #sub -1 to omit an extra partition at i==n (A |B | C |<-)
        return self.memo(0,n,s,dp) - 1
        
        
    def memo(self, i : int, n: int, s:str, dp: List[int]) -> int:
        #base case
        if (i == n):
            return 0
        
        #check visited
        if dp[i] != -1:
            return dp[i]
        
        #init mincuts
        mincost = float("inf")
        
        for j in range(i,n):
            #palindrome check of substr from i...j (if (i..j) is palindrome, then cut)
            if (s[i:j] == s[j:i:-1]):
                cost = 1 + self.memo(j+1, n, s, dp)
                mincost = min(mincost,cost)
                
        dp[i] = mincost
        
        return dp[i]
      
      
  '''
TABULATION - TOP DOWN
TIME- O(N^2)
SPACE - O(N)
'''
  
  class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        #in tab always take an extra dim for base cases
        dp = [0] * (n+1)
        
        #base case
        dp[n] = 0
        
         
        #bottom up tabulation
        for i in range(n-1,-1,-1):
            mincost = float("inf")
            for j in range(i,n):
                if (s[i:j] == s[j:i:-1]):
                    cost = 1 + dp[j+1]
                    mincost = min(mincost,cost)
            dp[i] = mincost
        
        return dp[0] - 1
    
    
       
            
