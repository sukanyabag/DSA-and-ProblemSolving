'''
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #cool af
        s.reverse()
        
  #brainly  
  class Solution:
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)
      
    #pythonic
    class Solution:
    def reverseString(self, s):
        return s[::-1]
      
