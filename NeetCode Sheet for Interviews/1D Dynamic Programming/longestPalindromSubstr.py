'''
Given a string s, return the longest 
palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

#TABULATION
# TC - O(N^2)
# SC - O(N^2)

def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal with True
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]

        return longest_palindrom
      
#TWO POINTER APPROACH -----DO THIS------
# TC - O(N^2)
# SC - O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.length = 0

        def buildPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > self.length:
                    self.res = s[l: r + 1]
                    self.length = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # For odd length
            l, r = i, i
            buildPalindrome(l, r)

            # For even length
            l, r = i, i + 1
            buildPalindrome(l, r)
        
        return self.res


