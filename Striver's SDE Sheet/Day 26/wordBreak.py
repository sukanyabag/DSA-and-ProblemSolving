'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
'''
TABULATED BOTTOM UP DP

TIME COMPLEXITY - O(N^2 * M) (N(LEN OF STR)*M(LEN OF DICT) * N(FOR CHECKING IF WORD IN DICT LIES IN STR) )
SPACE COMPLEXITY - O(N)
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        #bottom up
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if(i + len(w) <= len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                    
                if dp[i]:
                    break
                    
        return dp[0]
