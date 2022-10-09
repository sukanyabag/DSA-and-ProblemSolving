'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m non-empty substrings respectively, such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
'''
'''
MEMOIZATION
TC - O(M X N)
SC - O(M X N) + AUXILLARY STACK SPACE
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            dp[(i,j)] = False
            return False
        
        return dfs(0,0)


'''
TABULATION
TC - O(M X N)
SC - O(M X N)
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        p = len(s3)
        
        if (n + m) != p:
            return False
        
        dp = [[False] * (m+1) for _ in range(n+1)]
        
        dp[n][m] = True
        
        for i in range(n,-1,-1):
            for j in range(m, -1,-1):
                if i < n and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < m and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                    
        return dp[0][0]
