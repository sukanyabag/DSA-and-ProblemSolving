'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:
Insert a character
Delete a character
Replace a character
 
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''
#MEMOIZATION - TC - O(N*M),SC - O(N*M) + O(N+M)
class Solution:
    def solve(self, text1, text2, idx1, idx2, dp):
        
        if idx1 == 0:
            return idx2
        
        if idx2 == 0:
            return idx1
        
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        if text1[idx1-1] == text2[idx2-1]:
            dp[idx1][idx2] = self.solve(text1, text2, idx1-1, idx2-1, dp)
            return dp[idx1][idx2]
        
        dp[idx1][idx2] = 1 + min(self.solve(text1, text2, idx1, idx2-1, dp),
                                 self.solve(text1, text2, idx1-1, idx2, dp),
                                 self.solve(text1, text2, idx1-1, idx2-1, dp))
        
        return dp[idx1][idx2]
        
        
#  Insert Op ________ self.solve(text1, text2, idx1, idx2-1)
#  Delete Op ________ self.solve(text1, text2, idx1-1, idx2)
#  Replace Op ________ self.solve(text1, text2, idx1-1, idx2-1)


    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        if word1 == word2:
            return 0
        for _ in range(len(word1)+1):
            arr = []
            for _ in range(len(word2)+1):
                arr.append(-1)
            dp.append(arr)
        
        ans = self.solve(word1, word2, len(word1), len(word2), dp)
        return ans
      
      
      
#TABULATION - TC - O(N*M),SC - O(N*M)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        #base case - if any str is empty, take length of the other non-empty string
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
            
            
        #main logic - if char same, increment both i and j pointer. Otherwise, perform 
        #insert, replace delete ops and take min of them 
        
        #bottomup (tabulation)
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                #matches
                if word1[i] == word2[j]:
                    cache[i][j] = 0 + cache[i+1][j+1]
                    
                #not matches
                 '''
                insert = (i,j+1)
                delete = (i+1, j)
                replace = (i+1. j+1)
                
                each takes 1 cost per operation
                '''
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], 
                                          cache[i][j+1], 
                                          cache[i+1][j+1])
                    
       
      return cache[0][0]
            
        
