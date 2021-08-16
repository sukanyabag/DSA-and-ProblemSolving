'''
Given a string s, reverse only all the vowels in the string and return it.The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 
Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a','e','i','o','u','A','E','O','I','U'}
        
        s = list(s)
        
        vpos = []
        vchar = []
        
        for index, char in enumerate(s):
            if char in vowel:
                vpos.append(index)
                vchar.append(char)
                
        for i in vpos:
            s[i] = vchar.pop()
            
        return "".join(s)
            
        
