'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) 
of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''
'''
MEMOIZATION
TC - O(M*N)
SC - O(M*N) + AUXILLARY STACK SPACE
M,N - LENGTHS OF S AND T
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]
      
      
'''
TABULATION
TC - O(M*N)
SC - O(M*N) 
M,N - LENGTHS OF S AND T
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
        
        """not reqd as dp table initialised with zero"""
        # for i in range(1, n+1): 
        # dp[0][i] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]	#if current character is used
                #if current character is skipped
                dp[i][j] += dp[i-1][j] 
        return dp[-1][-1]
                
