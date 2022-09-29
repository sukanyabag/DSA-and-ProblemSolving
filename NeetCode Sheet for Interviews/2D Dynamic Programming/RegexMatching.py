'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''

#MEMOIZATION - TC - O(N*M), SC- O(N*M)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            #check match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # j+1 because pattern never starts with a * (check constraint)
            if (j+1) < len(p) and p[j+1] == '*':
                #if not matches, shift j by 2 (i same), to avoid considering '*' regex char
                # if matches, then check if it's a match and increment i by 1, keep j same
                
                dp[(i,j)] = (dfs(i, j+2) or #don't use '*'
                        (match and dfs(i+1,j))) # use '*'
                    
                return dp[(i,j)]
            
            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            
            dp[(i,j)] = False
            return False
        
        return dfs(0,0)
                
                
